      var all_searches = document.getElementsByTagName("search");      
      var help_dict = {};
      for ( var i = 0; i < all_searches.length; i++ ) {
          // Organize the help
          var help_id = all_searches[i].id;
          var help = document.querySelectorAll("searchhelp[id='" + help_id + "']");
          help_dict[help_id] = {}
          if (help.length > 0) { // We want to know if we have an existing id.
              for ( var li = 0; li < help.length; li++ ) {
                  var item = help[li];
                  var searchhelp = item.innerHTML;
                  var searchhelp_items = searchhelp.split(";");
                  var outhtml = "<table id=\"splhelp\">\n";
                  outhtml += "<tr>\n";
                  outhtml += "  <th> Splunk Search </th>";
                  outhtml += "  <th> Help </th>";
                  outhtml += "</tr>\n";

                  // Usually there should be only one, but who knows!
                  for ( var e = 0; e < searchhelp_items.length; e++ ) {
                      var pos_str_rex = /\s*(\d+)\s*:\s*(.*)/i;
                      var pos_str = searchhelp_items[e].match(pos_str_rex);                      
                      if (pos_str && (pos_str.length > 1)) {
                          help_dict[help_id][pos_str[1]] = pos_str[2];
                      } else {
                           console.log("Error: the description string must contain the position number, such as '1: foobar' or '2-4:blah'; Instead we got: " + searchhelp_items[e]);
                      }
                      
                  }
              }

              // console.log(help_dict)
              
              // Process the searches
              search = document.querySelectorAll("search[id='" + help_id + "']");
              if (search.length > 0) {
                  for ( var li = 0; li < search.length; li++ ) {
                      var item = search[li];
                      search_str = item.innerHTML;
                      search_str_elements = search_str.split("|");
                      // reassembled_search_str = null;
                      // number_of_items_reassembled = 0;
                      for ( var e = 1; e < search_str_elements.length; e++ ) {
                          // if (help_dict[help_id][e + 2] < help_dict[help_id].length) {
                          // }
                          outhtml += "<tr>\n";
                          outhtml += "  <td width=\"60%\"> |" + search_str_elements[e] + "</td>";
                          outhtml += "  <td id=\"help\">" + help_dict[help_id][e] + "</td>";
                          outhtml += "</tr>\n";
                      }                      
                  }
              }              

              outhtml += "</table>\n";
              item.innerHTML = outhtml;

          } else { // if (help.length > 0)
              console.error("The search id '" + all_searches[i].id + "' does not have the <searchhelp> tag with the corresponding id!");
              all_searches[i].innerHTML = "";
          }
      }
      
      // We clean the help tags
      var all_helps = document.getElementsByTagName("searchhelp");
      for (var i = 0; i < all_helps.length; i++ ) {
          all_helps[i].innerHTML = "";
      }
