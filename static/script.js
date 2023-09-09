

async function printData (url, cols) {

    let container = document.getElementById("container");
    const response = await fetch(url);

    try {
        const jsonData = await response.json();
        
        let table = document.createElement("table");
        let thead = document.createElement("thead");
        let tr = document.createElement("tr");
        
            table.classList.add(..."w-full text-sm text-left text-blue-900 dark:text-gray-400".split(" "))
            thead.classList.add(...'text-xs text-blue-900 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400'.split(" "))

        cols.forEach((item) => {
            let th = document.createElement("th");
            th.innerText = item;
            th.classList.add(...'px-6 py-3'.split(" "))
            tr.appendChild(th);
        });
        thead.appendChild(tr);
        table.append(thead)
        
        let tbody = document.createElement("tbody");

        jsonData.forEach((item) => {
            let tr = document.createElement("tr");
            tr.classList.add(...'bg-white border-b dark:bg-gray-800 dark:border-gray-700'.split(" "))
            let vals = Object.values(item);
            
            vals.forEach((elem) => {
                let td = document.createElement("td");
                td.classList.add(...'px-6 py-3'.split(" "))

                if (isNaN(elem)) {
                    td.innerText = elem;
                } else {
                    td.innerText = Number( elem.toPrecision(6) );
                }
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
        table.append(tbody)
        container.appendChild(table)

    } catch (error) {
        console.error(response)

        let error_div = document.createElement("div");
        error_div.innerText = "Failed to calculate emissions for flights";
        error_div.classList.add(...'px-6 py-3 w-full text-sm text-left text-red-800 dark:text-red-400'.split(" "))
        container.appendChild(error_div)
    }
}

async function printTaskData () {
    const url = "http://" + window.location.host + "/api/tasks"
    let cols = ["Name"]
    printData(url, cols)
}

if (window.location.pathname == "/") {
    printTaskData()
}
