async function callGetAllEndpoint() {
    console.log("START")

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
    const output_table = document.getElementById("output_table")!
    let columRow = 0
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

        columRow++
    }

    document.getElementById("table_wrapper")!.appendChild(output_table)
    console.log(`END - ${fetches.length} queries was runned successfully`)
}