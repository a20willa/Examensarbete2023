async function callGetAllEndpoint() {
    // Tell user that the test is running
    document.getElementById("running")!.innerHTML = "Running test, please wait..."

    // Variables
    const fetches = []
    const itterationsInput = document.getElementById("itterations") as HTMLInputElement
    const database = (document.getElementById("database") as HTMLSelectElement).value

    // Go trough itterations
    for (var i = 0; i < Number(itterationsInput.value); i++) {
        try {
            fetches.push(await fetch(
                'http://127.0.0.1:3000/' + database,
                {
                    method: 'GET',
                    mode: 'cors',
                },
            ))
        } catch (e) {
            throw new Error(String(e))
        }
    }

    
    // Get response and print them at the end
    const responses = await Promise.all(fetches)
    // Create table
    const output_table = document.getElementById("output_table")!
    // To show index in table
    let columRow = 0

    // Go trough all resposes and append table attributes
    for (const response of responses) {
        // Create index attribute
        const index = document.createElement("td")
        index.innerText = String(columRow)

        // Create URL attribute
        const url = document.createElement("td")
        url.innerText = response.url

        // Create ok attribute
        const ok = document.createElement("td")
        ok.innerText = String(response.ok)

        // Create row in table
        const row = document.createElement("tr")
        row.append(index, url, ok)
        output_table.appendChild(row)

        // Increase the index
        columRow++
    }

    // Remove test text as to leave room for the table
    document.getElementById("running")!.remove()
    
    // Finally, append the table
    document.getElementById("table_wrapper")!.appendChild(output_table)
}