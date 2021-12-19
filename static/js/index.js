const scrape = async () => {
    let plac = document.getElementById("bulliten");
    console.log("hello tehre")
    let data = await fetch('http://127.0.0.1:8000/scrape');     
    let data2 = await data.json();
    
    for(let i of data2){
        let node = document.createElement('a')
        node.setAttribute("class","bull")
        node.innerText = i[0];
        node.href = `https://economictimes.indiatimes.com/${i[1]}`
        plac.appendChild(node);
        console.log(i)
        
    }
}
scrape();

