function getNetworkHAR() {
    browser.devtools.network.getHAR().then((har) => {
        const harString = JSON.stringify(har);
        const file = new Blob([harString], {type: 'application/json'});
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