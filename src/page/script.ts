async function callGetAllEndpoint() {
    console.log("START")
    const fetches = []
    const itterationsInput = document.getElementById("itterations") as HTMLInputElement
    const database = (document.getElementById("database") as HTMLSelectElement).value

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

    await Promise.all(fetches)
    console.log(`END - ${fetches.length} queries was runned successfully`)
}