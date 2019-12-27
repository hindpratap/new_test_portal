// Question string
try{
    let questData = document.querySelectorAll('.quest-data');
    // console.log(questData.innerHTML.length);
    [...questData].map(e => {
        if(e.innerHTML.length > 32){
            e.innerHTML = e.innerHTML.slice(0, 30) + `...`;
        }
    })
}catch(err){
    console.error('error in quest string');
}

