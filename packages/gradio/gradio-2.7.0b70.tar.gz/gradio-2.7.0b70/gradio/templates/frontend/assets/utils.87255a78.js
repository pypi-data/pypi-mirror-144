const c=(t,o=250)=>{let e=null;return(...n)=>{const u=()=>t(...n);e&&clearTimeout(e),e=setTimeout(u,o)}};export{c as d};
