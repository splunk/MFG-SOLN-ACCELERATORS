require([
    'jquery',
    'underscore',
    'splunkjs/mvc/simplexml/controller',
    'splunk.util',
    'backbone',
    'collections/shared/Dashboards',
    'bootstrap.affix',
    'bootstrap.scrollspy'
], function($, _, DashboardController, SplunkUtil, Backbone, DashboardsCollection) {

    var HIDE_MISSING_VIEWS = false;

    DashboardController.onReady(function() {

        DashboardController.onViewModelLoad(function() {
            var app = DashboardController.model.app.get('app');
            var view = DashboardController.model.view;
            var dashboards = new DashboardsCollection();
            var dashboardsLoaded = dashboards.fetch({ data : { app: app, owner: '-', count: 0 } });
            var exampleInfoCollection = new Backbone.Collection();
            var categoriesCollection = new Backbone.Collection();
            
            var exampleInfoLoaded = exampleInfoCollection.fetch({
                url: SplunkUtil.make_url('/static/app/' + app +'/exampleInfo.json'),
                cache: true
            });
            var categoriesLoaded = categoriesCollection.fetch({
                url: SplunkUtil.make_url('/static/app/' + app +'/categories.json'),
                cache: true
            });
            // categoriesCollection.each(function(model, index, list) {
            //     console.log(model.get("category"));
            // });
            
            $.when(exampleInfoLoaded, categoriesLoaded, dashboardsLoaded).then(function(){
                var categories = _.uniq(exampleInfoCollection.pluck('category'));
                var $nav = $('<ul class="nav nav-list"></ul>').data('offset-top', "50");
                var $contents = $('<div class="example-contents"></div>');                
                var category_html = "";
                _.each(categories, function(category){
                    category_html = ""; // Clear
                    // FIXME: I should not run each, but find a way to extract all my objects from a category name
                    categoriesCollection.each(function(model, index, list) {
                        categories_category = model.get("category");
                        if (category.toLowerCase() == categories_category.toLowerCase()) {
                            category_description = model.get("description");
                            var inputid = category.replace(/ /g,"_").toLowerCase();
//                            console.log(inputid);
                            category_html = '<div class="wrap-collabsible"><input id="' + inputid + '" class="toggle" type="checkbox"/><label for="' + inputid + '" class="lbl-toggle">Description</label><div class="collapsible-content"><div class="content-inner">' + category_description + '</div></div></div>';
                        }
                    });
                    
                    var categoryFiltered = exampleInfoCollection.filter(function(exampleInfo) {
                        return exampleInfo.get("category") === category;
                    });
                    $nav.append($('<li></li>').append($('<a ></a>').attr('href', '#' + category.replace(/ /g,"_")).text(category)));
                    var categoryInfoCollection = new Backbone.Collection(categoryFiltered);                    
//                    console.log(category);
                    var $category= $('<section></section>').attr('id', category.replace(/ /g,"_"));
//                    console.log(category_html);
                    $category.append($("<h2></h2>").text(category)).append(category_html);
                    var $categoryContents = $('<div class=""></div>').appendTo($category);
                    categoryInfoCollection.each(function(exampleInfo){
                        var id = exampleInfo.get('id');
                        var $example = $('<a class="example"></a>').attr('href', id);
                        var view = dashboards.find(function(m){ return m.entry.get('name') === id; });
                        if(!view) {
                            if(HIDE_MISSING_VIEWS) { return; }
                            $example.addClass('missing').attr("title", "Example view is not available!");
                        }
                        var label = exampleInfo.get('title') || (view && view.entry.content.get('label') || id);
                        var $exampleTitle = $('<h3></h3>').text(label);
                        var $exampleImg = $('<img />').attr('src', SplunkUtil.make_url('/static/app/' + app +'/icons/' + (exampleInfo.get('description-icon') || exampleInfo.get('id') + ".png")));
                        var $exampleDescription = $('<p></p>').html(exampleInfo.get('short-description'));
                        var $exampleContent = $('<div class="content"></div>').append($exampleTitle).append($exampleDescription);
                        var $tags =  $('<div classh="tags"></div>').appendTo($exampleContent);
                        _.each(exampleInfo.get('tags'), function(tag){
                            var tagTitle = tag;
                            if (tag === "extension") {
                                tagTitle = _("Uses external JS/CSS").t();
                            }
                            $tags.append($('<span class="label"></span>').attr('title', tagTitle).tooltip().text(tag));
                        });
                        $example.append($exampleImg).append($exampleContent);
                        $categoryContents.append($example);
                    });
                    $contents.append($category);
                });
                $('.dashboard-body').append($('<div class="row contents-body"></div>').append($('<div class="nav-bar-slide"></div>').append($nav)).append($contents));
                $nav.affix({
                    offset: { top: $nav.offset().top }
                })
                $('body').scrollspy();
            });

        });

    });

});
