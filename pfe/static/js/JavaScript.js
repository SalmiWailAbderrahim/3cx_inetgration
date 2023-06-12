const searchBar = document.getElementById("searchBar");
        searchBar.addEventListener("keyup", function() {
          const filter = searchBar.value.toUpperCase();
          const table = document.getElementById("myTable");
          const rows = table.getElementsByTagName("tr");
          
          for (let i = 1; i < rows.length; i++) {
            const cells = rows[i].getElementsByTagName("td");
            let found = false;
            
            for (let j = 1; j < cells.length; j++) {
              const cell = cells[j];
              if (cell) {
                const cellValue = cell.textContent || cell.innerText;
                if (cellValue.toUpperCase().indexOf(filter) > -1) {
                  found = true;
                  break;
                }
              }
            }
            
            if (found) {
              rows[i].style.display = "";
            } else {
              rows[i].style.display = "none";
            }
          }
        });

      