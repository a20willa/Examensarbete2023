function getNetworkHAR() {
    browser.devtools.network.getHAR().then((har) => {
        // Create object to store relevant data
        const harString = {values: []}

        // Only get relevant results
        for(entry in har.entries){
            if(entry.request.url.includes("getAll")) {
                harString.values.push({time: entry.time, request: entry.request});
            }
        }

        // Construct and download file
        const file = new Blob([JSON.stringify(harString)], {type: 'application/json'});
        const a = document.createElement('a');
        a.href = URL.createObjectURL(file);
        a.download = 'geospatial_test_data.json';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    });
  }
  
  browser.devtools.panels.create("Get HAR", "icon.png", "panel.html", (panel) => {
    panel.onShown.addListener((window) => {
      const button = window.document.createElement("button");
      button.textContent = "Get Network HAR";
      button.addEventListener("click", getNetworkHAR);
      window.document.body.appendChild(button);
    });
  });