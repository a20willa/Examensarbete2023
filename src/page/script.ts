async function callGetAllEndpoint() {
    // Tell user that the test is running
    document.getElementById("running")!.innerHTML = "Running test, please wait..."

    // Variables
    const fetches = []
    const itterationsInput = document.getElementById("itterations") as HTMLInputElement
    const database = (document.getElementById("database") as HTMLSelectElement).value
    let times = []

    // Go trough itterations
    for (var i = 0; i < Number(itterationsInput.value); i++) {
        let fetch_time = { "start": 0, "end": 0 }
        try {
            fetch_time.start = Number(Date.now())
            fetches.push(await fetch(
                'http://127.0.0.1:3000/' + database + '?cache=' + Math.random(),
                {
                    method: 'GET',
                    mode: 'cors',
                },
            ))
            fetch_time.end = Number(Date.now())
            times.push(Math.abs(fetch_time.end - fetch_time.start))
        } catch (e) {
            throw new Error(String(e))
        }
    }

    // Get response and print them at the end
    const responses = await Promise.all(fetches)
    // Create table
    const output_table = document.getElementById("output_table")!
    // Get the tbody and reset it
    const tbody = document.getElementById("tbody")!
    tbody.innerHTML = ""
    // To show index in table
    let columRow = 0
    // Error value to say that something failed
    let err = false
    // Datatype
    let store_datatype = ""

    // Go trough all resposes and append table attributes
    for (const response of responses) {
        let json = ""

        try {
            json = JSON.stringify(await response.json())
        } catch (e) {
            err = true
            break;
        }

        console.log(json)

        // Create index attribute
        const index = document.createElement("td")
        index.innerText = String(columRow)

        // Create URL attribute
        const url = document.createElement("td")
        url.innerText = response.url

        // Create ok attribute
        const ok = document.createElement("td")
        ok.innerText = String(response.ok)

        // Create data attribute
        const data = document.createElement("td")
        const dataText = document.createElement("textarea")
        data.appendChild(dataText)

        // Create amount of items attriubte
        const amountOfItems = document.createElement("td")
        amountOfItems.innerText = JSON.parse(json).response.length

        // Create datatype attribute
        const datatype = document.createElement("td")
        try {
            if (database == "getAllMongodb") {
                datatype.innerText = JSON.parse(json).response[0].loc.type
                store_datatype = JSON.parse(json).response[0].loc.type
            }
            else {
                datatype.innerText = JSON.parse(json).response[0].type
                store_datatype = JSON.parse(json).response[0].type
            }
        } catch (e) {
            datatype.innerText = "No data"
        }

        // Dont show data if there is too much
        if (String(json).length < 9999) {
            dataText.value = String(json)
        } else {
            dataText.value = "Too much data to display"
        }

        // Create row in table
        const row = document.createElement("tr")
        row.append(index, url, ok, data, amountOfItems, datatype)
        tbody.appendChild(row)

        // Increase the index
        columRow++
    }

    // Save times to file with a anchor tag
    const database_name = (document.getElementById("database") as HTMLSelectElement).value == "getAllMongodb" ? "mongodb" : "mysql"
    const timesFile = new File([JSON.stringify(times)], `times_${database_name}_${store_datatype}.json`, { type: "text/plain;charset=utf-8" })
    const timesFileURL = URL.createObjectURL(timesFile)
    const timesFileAnchor = document.createElement("a")
    timesFileAnchor.href = timesFileURL
    timesFileAnchor.download = `times_${database_name}_${store_datatype}.json`
    timesFileAnchor.click()

    if (err) {
        document.getElementById("running")!.innerHTML = "An error occured (are you using the correct database?)"
    } else {
        // Remove test text as to leave room for the table
        document.getElementById("running")!.innerHTML = "Done!"
    }

    // Finally, append the table
    document.getElementById("table_wrapper")!.appendChild(output_table)
}