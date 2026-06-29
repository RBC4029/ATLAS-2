<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Atlas v0.2</title>
<style>
body{font-family:Arial;margin:0;background:#eef3f8;color:#172033}
header{background:#0f172a;color:white;padding:18px 24px}
main{max-width:1200px;margin:25px auto;display:grid;grid-template-columns:1fr 1fr;gap:18px}
.card{background:white;border-radius:14px;padding:20px;box-shadow:0 6px 18px rgba(0,0,0,.08)}
textarea{width:100%;height:340px;border:1px solid #cbd5e1;border-radius:10px;padding:12px}
button{background:#2563eb;color:white;border:0;border-radius:8px;padding:12px 16px;font-weight:bold;margin-top:10px;cursor:pointer}
pre{white-space:pre-wrap;background:#f8fafc;border:1px solid #e5e7eb;border-radius:10px;padding:14px}
.small{font-size:13px;color:#64748b}
</style>
</head>
<body>
<header><h2>Atlas v0.2 — Copilote de pré-instruction</h2></header>
<main>
<section class="card">
<h3>Déclaration</h3>
<p class="small">Cette page fonctionne en local. Si le backend tourne sur http://localhost:8000, elle appelle l'API. Sinon elle affiche une analyse locale simplifiée.</p>
<textarea id="txt">Dégât des eaux le 12/06/2026 au 12 rue Victor Hugo. Fuite du voisin du dessus. Photos et devis 2350 euros.</textarea>
<button onclick="analyze()">Analyser</button>
<button onclick="saveClaim()">Créer dossier dans API</button>
</section>
<section class="card">
<h3>Résultat</h3>
<pre id="out">En attente.</pre>
</section>
</main>
<script>
async function analyze(){
 const text=document.getElementById("txt").value;
 try{
   const res=await fetch("http://localhost:8000/api/v1/claims/analyze",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({claim_id:"DEMO-"+Date.now(),text,contract_active:true})});
   const data=await res.json();
   document.getElementById("out").textContent=JSON.stringify(data,null,2);
 }catch(e){
   document.getElementById("out").textContent="Backend non lancé. Lance uvicorn pour utiliser l'API.\n\n"+e;
 }
}
async function saveClaim(){
 const text=document.getElementById("txt").value;
 try{
   const res=await fetch("http://localhost:8000/api/v1/claims",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({claim_id:"D-"+Date.now(),text,contract_active:true})});
   const data=await res.json();
   document.getElementById("out").textContent=JSON.stringify(data,null,2);
 }catch(e){
   document.getElementById("out").textContent="Backend non lancé. Impossible de créer le dossier.\n\n"+e;
 }
}
</script>
</body>
</html>