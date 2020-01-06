// Info title
let infoTitle = document.querySelector('.info-title');
infoTitle.title = `
Password must contain 
1.Uppercase letter 
2.Lowercase letter 
3.Number 
4.Special Character 
5.Password-length must be 8-10 Character`;

/*--- Form Validation
------------------------------------*/

// Regex
let passRegx = new RegExp(/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@\$\^\*])(?=.{8,})/);
let emailRegx = new RegExp(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/);
let mobileRegx = new RegExp(/^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/);

try{
    let credForm = document.querySelector('.cred-form');
    let formElem = credForm.querySelectorAll('.form-elem');

    //User Validation
    let user = credForm.querySelector('.form-elem--user');
    user.addEventListener('focusout', ()=>{
        duplicateChecker(user);
    });

    // Password Validation
    let pass = credForm.querySelector('.form-elem--pass');
    let lenArr = [8, 9, 10];
    let len = lenArr[Math.floor(Math.random() * lenArr.length)];
    pass.value = password_generator(len);

    // Email Validation
    let email = credForm.querySelector('.form-elem--email');
    email.addEventListener('keyup', ()=>{
        if(validator(email)){
            duplicateChecker(email);
        }else if(email.value === ``){
            email.parentElement.querySelector('.note').innerHTML = '';
            email.style = `border: 1px solid tomato; background: #ffeae6;`;
        }else{
            email.parentElement.querySelector('.note').innerHTML = '';
            email.style = `border: 1px solid tomato; background: #ffeae6;`;
        }
    });

    // Phone Validation
    let mobile = credForm.querySelector('.form-elem--mobile');
    mobile.addEventListener('keyup', ()=>{
        if(validator(mobile)){
            duplicateChecker(mobile);
        }
    });

    // Submit Button
    const credSubmit = document.querySelector('#credForm');
    credSubmit.addEventListener('submit', e => {
        let fOpt;
        [...formElem].map(f=>{
            const dataID = f.getAttribute('data-id');
            switch(dataID){
                case 'name':
                    if (f.value === ``){
                        e.preventDefault();
                        f.parentElement.querySelector('.note').innerHTML = 'Please Enter Full Name of user';
                        f.style = `border: 1px solid tomato; background: #ffeae6;`;
                    }else{
                        f.parentElement.querySelector('.note').innerHTML = '';
                        f.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
                    }
                    break;

                case 'username':
                    if(duplicateChecker(user)){
                        e.preventDefault();
                    }
                    break;

                case 'pass':
                    if (f.value === ``){
                        e.preventDefault();
                        f.parentElement.querySelector('.note').innerHTML = 'Please provide password';
                        f.style = `border: 1px solid tomato; background: #ffeae6;`;
                    }else if(passRegx.test(f.value)){
                        f.parentElement.querySelector('.note').innerHTML = '';
                        f.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
                    }else{
                        e.preventDefault();
                        f.parentElement.querySelector('.note').innerHTML = 'Password does not match the guidelines';
                        f.style = `border: 1px solid tomato; background: #ffeae6;`;
                    }
                    break;

                case 'email':
                    if(validator(f)){
                        if(duplicateChecker(email)){
                            e.preventDefault();
                        }
                    }else{
                        e.preventDefault();
                        f.parentElement.querySelector('.note').innerHTML = 'Please provide correct email-id';
                        f.style = `border: 1px solid tomato; background: #ffeae6;`;
                    }
                    break;

                case 'mobile':
                    if(validator(mobile)){
                        if(duplicateChecker(mobile)){
                            e.preventDefault();
                        }
                    }else{
                        e.preventDefault();
                        f.parentElement.querySelector('.note').innerHTML = 'Please provide correct phone number';
                        f.style = `border: 1px solid tomato; background: #ffeae6;`;
                    }
                    break;

                case 'dob':
                    if (f.value === ``){
                        e.preventDefault();
                        f.parentElement.parentElement.querySelector('.note').innerHTML = 'Please provide date of birth';
                        f.style = `border: 1px solid tomato; background: #ffeae6;`;
                    }else{
                        f.parentElement.parentElement.querySelector('.note').innerHTML = '';
                        f.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
                    }
                    break;

                case 'position':
                    fOpt = f.options[f.selectedIndex].value;
                    if (fOpt === ``){
                        f.parentElement.querySelector('.note').innerHTML = 'Please select a position for candidate';
                        f.style = `border: 1px solid tomato; background: #ffeae6;`;
                        e.preventDefault();
                    }else{
                        f.parentElement.querySelector('.note').innerHTML = '';
                        f.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
                    }
                    break;

                case 'team':
                    fOpt = f.options[f.selectedIndex].value;
                    if (fOpt === ``){
                        e.preventDefault();
                        f.parentElement.querySelector('.note').innerHTML = 'Please select a team for candidate';
                        f.style = `border: 1px solid tomato; background: #ffeae6;`;
                    }else{
                        f.parentElement.querySelector('.note').innerHTML = '';
                        f.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
                    }
                    break;

                case 'location':
                    fOpt = f.options[f.selectedIndex].value;
                    if (fOpt === ``){
                        e.preventDefault();
                        f.parentElement.querySelector('.note').innerHTML = 'Please select a location';
                        f.style = `border: 1px solid tomato; background: #ffeae6;`;
                    }else{
                        f.parentElement.querySelector('.note').innerHTML = '';
                        f.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
                    }
                    break;

                case 'source':
                    fOpt = f.options[f.selectedIndex].value;
                    if (fOpt === ``){
                        e.preventDefault();
                        f.parentElement.querySelector('.note').innerHTML = 'Please select a location';
                        f.style = `border: 1px solid tomato; background: #ffeae6;`;
                    }else{
                        f.parentElement.querySelector('.note').innerHTML = '';
                        f.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
                    }
                    break;

                case 'resume':
                    if (f.value === ``){
                        e.preventDefault();
                        f.parentElement.querySelector('.note').innerHTML = 'Please upload a resume of candidate';
                        f.parentElement.querySelector('.custom-file-label').style = `border: 1px solid tomato; background: #ffeae6;`;
                    }else{
                        f.parentElement.querySelector('.note').innerHTML = '';
                        f.parentElement.querySelector('.custom-file-label').style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
                    }
                    break;

                default:
                    console.log('bye');
            }
        })
    });

    if(passRegx.test(pass.value)){
            pass.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
            pass.readOnly = true;
    }

}catch(err){
    console.error('hey error');
}

let validator = (arg) => {

    /*  Getting data-id of the element calling the function adding 'Regex' to the id
        Calling eval to evaluate string as a variable storing valid js (in this case Regex)
        Checking whether the element input follows regex or not
    */

    let argID = arg.getAttribute('data-id') + 'Regx';
    let argRegx = eval(argID);
    if(argRegx.test(arg.value)){
        arg.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
        return true;
    }else{
        arg.style = `border: 1px solid tomato; background: #ffeae6;`;
        return false;
    }

};

let duplicateChecker = (dup)=>{
    let dupMed = dup.getAttribute('data-id');
    let dupID = dupMed + 'Dup';
    let dupVal = eval(dupID);
    let flag = false;

    for(let i=0; i<dupVal.length; i++){
        if(dup.value === dupVal[i]){
            dup.parentElement.querySelector('.note').innerHTML = `${dupMed} already exists!`;
            dup.style = `border: 1px solid tomato; background: #ffeae6;`;
            flag = true;
            break;
        }else if(dup.value === ``){
            dup.parentElement.querySelector('.note').innerHTML = `Please provide ${dupMed}`;
            dup.style = `border: 1px solid tomato; background: #ffeae6;`;
            flag = false;
        }
        else{
            dup.parentElement.querySelector('.note').innerHTML = ``;
            dup.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
            flag = false;
        }
    }

    return flag;
};

function password_generator( len ){
    let length = (len)?(len):(10);
    let string = "abcdefghijklmnopqrstuvwxyz"; //to upper
    let numeric = '0123456789';
    let punctuation = '!@$%^*';
    let password = "";
    let character = "";
    let crunch = true;
    while( password.length<length ) {
        entity1 = Math.ceil(string.length * Math.random()*Math.random());
        entity2 = Math.ceil(numeric.length * Math.random()*Math.random());
        entity3 = Math.ceil(punctuation.length * Math.random()*Math.random());
        hold = string.charAt( entity1 );
        hold = (password.length%2==0)?(hold.toUpperCase()):(hold);
        character += hold;
        character += numeric.charAt( entity2 );
        character += punctuation.charAt( entity3 );
        password = character;
    }
    password=password.split('').sort(function(){return 0.5-Math.random()}).join('');
    return password.substr(0,len);
};
