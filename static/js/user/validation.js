/* User Signup Form validation */

try{
    const signUpForm = document.querySelector('.signup-form');
    const elem = signUpForm.querySelectorAll('.form-elem');
    let fOpt;

    signUpForm.addEventListener('submit', (e) => {
        [...elem].forEach(f => {
            const dataId = f.getAttribute('data-id');

            switch(dataId){
                case 'name':
                    if(dup(f)){
                        e.preventDefault();
                    }
                    break;

                case 'username':
                    if(dup(f)){
                        e.preventDefault();
                    }
                    break;

                case 'pass':
                    if(dup(f)){
                        e.preventDefault();
                    }
                    break;

                case 'email':
                    if(dup(f)){
                        e.preventDefault();
                    }
                    break;

                case 'mobile':
                    if(dup(f)){
                        e.preventDefault();
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
                    if(dup(f)){
                        e.preventDefault();
                    }
                    break;

                default:
                    break;
            }

        })

    });

    const sr = signUpForm.querySelector('[data-id="source"]');
    const rf = signUpForm.querySelector('[data-id="referral"]');
    const bl = signUpForm.querySelector('.blank_');

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

}catch (e) {
    console.log(e);
}

function dup(b) {
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