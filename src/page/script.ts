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
    for (const response of responses) {
        const data = await response.json()
        console.log(data)
    }
    console.log(`END - ${fetches.length} queries was runned successfully`)
}