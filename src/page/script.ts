async function callGetAllEndpoint() {
    const fetches = []
    const itterationsInput = document.getElementById("itterations") as HTMLInputElement

    for (var i = 0; i < Number(itterationsInput.value); i++) {
        try {
            fetches.push(await fetch(
                'http://127.0.0.1:3000/getAll',
                {
                    method: 'GET',
                    mode: 'cors',
                },
            ).then(res => console.log(i)))

        } catch (e) {
            throw new Error(e + "Cannot fetch endpoint 'getAll', is the server runnning?")
        }
    }

    await Promise.all(fetches)
    console.log("Done!")
}