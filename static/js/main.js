
let searchform = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')
if (searchform){
    for (let i=0; i< pageLinks.length; i++){
        pageLinks[i].addEventListener('click', function(e){
            e.preventDefault()
            // get the data attribute
            let page=this.dataset.page
            // add input field in the search form
            searchform.innerHTML += `<input value=${page} name="page" hidden />`
            
            // submit the search form
            searchform.submit()

        })
    }
}


let projectUrl = "http://127.0.0.1:8000/api/remove-tag/"
let tags = document.getElementsByClassName('project-tag')
for (let i = 0; i <tags.length; i++){
    tags[i].addEventListener('click', (e) => {
        let tagId = e.target.dataset.tag
        let projectId = e.target.dataset.project
        
        fetch(projectUrl,
        {
            method:'DELETE',
            headers:{
                contentType: 'application/json'
            },
            body:JSON.stringify({'project':projectId, 'tag':tagId})
        })
        .then(response => response.json())
        .then(data =>{
            e.target.remove()
        })


    })
}



