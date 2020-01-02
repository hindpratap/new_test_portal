// Fetch Components
try{
    const passwordEye = document.querySelector(`.password-eye`);
    const passwordInput = document.querySelector(`[name='password']`);

    let passwordState = false;

    passwordEye.addEventListener('click', ()=>{
        console.log('work');
        if(passwordState){
            passwordEye.innerHTML = `<i class="fas fa-eye-slash"></i>`;
            passwordEye.setAttribute('title', 'Hide Password');
            passwordInput.setAttribute('type', 'password');
            passwordState = false;
        }else{
            passwordEye.innerHTML = `<i class="fas fa-eye"></i>`;
            passwordEye.setAttribute('type', 'Show Password');
            passwordInput.setAttribute('type', 'text');
            passwordState = true;
        }
    });
}catch(err){}

// Instruction Components
try{
    // Continue/Start
    const startBtn = document.querySelector('.start-test');
    const startDiv = document.querySelector('.starter');
    const cancelNo = document.querySelector('.cancel-no');

    startBtn.addEventListener('click', (e)=>{
        startDiv.style.visibility = 'visible';
        console.log('start');
    });

    cancelNo.addEventListener('click', (e)=>{
        startDiv.style.visibility = 'hidden';
        console.log('close');
    });

}catch(err){
    console.log('err');
}