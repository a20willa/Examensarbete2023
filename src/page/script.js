"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
function callGetAllEndpoint() {
    return __awaiter(this, void 0, void 0, function* () {
        const fetches = [];
        const itterationsInput = document.getElementById("itterations");
        for (var i = 0; i < Number(itterationsInput.value); i++) {
            try {
                fetches.push(yield fetch('http://127.0.0.1:3000/getAll', {
                    method: 'GET',
                    mode: 'cors',
                }).then(res => console.log(i)));
            }
            catch (e) {
                throw new Error(e + "Cannot fetch endpoint 'getAll', is the server runnning?");
            }
        }
        yield Promise.all(fetches);
        console.log("Done!");
    });
}
//# sourceMappingURL=script.js.map