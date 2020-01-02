// Navigation Active
let loc = window.location.pathname;
const pt  = {
    "/adminboard/adminhome/": "adminhome",
    "/adminboard/adminuser/": "adminuser",
    "/adminboard/addcredential/": "adminuser",
    "/adminboard/addquest/": "addquest",
    "/adminboard/viewquest/": "addquest",
    "/adminboard/submission/": "submissions"
};

for(let key in pt){
    if(pt.hasOwnProperty(key)){
        if(key === loc){
            document.querySelector(`.${pt[key]}`).classList.add('active');
        }
    }
}