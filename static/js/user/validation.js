// User Sign up form validation

const signupForm = document.querySelector('#credForm'),
      formElements = signupForm.querySelectorAll('.form-elem'),
      registerBtn = signupForm.querySelector('#register');

signupForm.addEventListener('submit', (e) => {
    let check = 1;
    console.log(check);

    formElements.forEach(f => {
        const dataId = f.getAttribute('data-id');

        switch(dataId){
            case 'name':
                if(duplicateCheck(f)){
                    e.preventDefault();
                    check++;
                }
                break;

            case 'username':
                if(duplicateCheck(f)){
                    e.preventDefault();
                    check++;
                }
                break;

            case 'pass':
                if(duplicateCheck(f)){
                    e.preventDefault();
                    check++;
                }
                break;

            case 'email':
                if(duplicateCheck(f)){
                    e.preventDefault();
                    check++;
                }
                break;

            case 'mobile':
                if(duplicateCheck(f)){
                    e.preventDefault();
                    check++;
                }
                break;

            case 'dob':
                if (f.value === ``){
                    e.preventDefault();
                    check++;
                    f.parentElement.parentElement.querySelector('.note').innerHTML = 'Please provide date of birth';
                    f.style = `border: 1px solid tomato; background: #ffeae6;`;
                }else{
                    f.parentElement.parentElement.querySelector('.note').innerHTML = '';
                    f.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
                }
                break;

            case 'location':
                fOpt = f.options[f.selectedIndex].value;
                if (fOpt === ``){
                    e.preventDefault();
                    check++;
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
                    check++;
                    f.parentElement.querySelector('.note').innerHTML = 'Please select a location';
                    f.style = `border: 1px solid tomato; background: #ffeae6;`;
                }else{
                    f.parentElement.querySelector('.note').innerHTML = '';
                    f.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
                }
                break;

            case 'resume':
                if(duplicateCheck(f)){
                    e.preventDefault();
                    check++;
                }
                break;

            default:
                break;

        }
    });

    console.log(check)
    if(check === 1){
        registerBtn.innerHTML=`<i class="fas fa-circle-notch load-icon"></i> Registering`;
        registerBtn.setAttribute('type', 'button');
    }
});

const sr = signupForm.querySelector('[data-id="source"]');
const rf = signupForm.querySelector('[data-id="referral"]');
const bl = signupForm.querySelector('.blank_');

sr.addEventListener('change', () => {
    fOpt = sr.options[sr.selectedIndex].value;
    if(fOpt === 'Referral'){
        rf.parentElement.classList.remove('hidden');
        bl.classList.add('hidden');
    }else{
        rf.parentElement.classList.add('hidden');
        bl.classList.remove('hidden');
    }
})

function duplicateCheck(b) {
    const bID = b.getAttribute('data-id');
    let v;
    let foo = false;
    (bID === 'username') ? v = u : (bID === 'email') ? v = m : v = p;
    if(v !== ''){
        v.forEach(s => {
        if(!foo){
            if(b.value === ''){
                b.parentElement.querySelector('.note').innerHTML = `Please provide a ${bID}`;
                b.style = `border: 1px solid tomato; background: #ffeae6;`;
                foo = true;
            }
            else if(b.value === s) {
                b.parentElement.querySelector('.note').innerHTML = `${bID} already exists!`;
                b.style = `border: 1px solid tomato; background: #ffeae6;`;
                foo = true;
            }else{
                b.parentElement.querySelector('.note').innerHTML = ``;
                b.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
            }
        }
    });
    }else{
        if(b.value === ''){
            b.parentElement.querySelector('.note').innerHTML = `Please provide a ${bID}`;
            b.style = `border: 1px solid tomato; background: #ffeae6;`;
            foo = true;
        }else{
            b.parentElement.querySelector('.note').innerHTML = ``;
            b.style = `border: 1px solid mediumaquamarine; background: #dbfdf1;`;
            foo = false;
        }
    }
    return foo;
}