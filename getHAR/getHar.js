function getNetworkHAR() {
    browser.devtools.network.getHAR().then((har) => {
        const harTimes = []
        
        for(const entry of har.entries) {
            harTimes.push(entry.time)
        }

        const file = new Blob([harTimes], {type: 'application/json'});
        const a = document.createElement('a');
        a.href = URL.createObjectURL(file);
        a.download = 'har-file.txt';
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