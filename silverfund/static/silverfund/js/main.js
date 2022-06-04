function mode(s){
    if(s=='Night'){
      document.querySelector('body').style.backgroundColor='#323232';
      document.querySelector('body').style.color='white';
      document.querySelector('nav ul').style.borderTopColor='white';
      document.querySelector('nav ul').style.borderBottomColor='white';
      var alist = document.querySelectorAll('a');
      var i = 0;
      while(i < alist.length){
        alist[i].style.color = 'white';
        i++;
      }
    }else if(s=='Day'){
      document.querySelector('body').style.backgroundColor='white';
      document.querySelector('body').style.color='black';
      document.querySelector('nav ul').style.borderTopColor='black';
      document.querySelector('nav ul').style.borderBottomColor='black';
      var alist = document.querySelectorAll('a');
      var i = 0;
      while(i < alist.length){
        alist[i].style.color = 'black';
        i++;
      }
    }
}
