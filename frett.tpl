<html>

<head>
	<title></title>
	<link rel="stylesheet" type="text/css" href="/staticskrar/app.css">
</head>

<body>

<div class="container">

<header>
   <h1>Fréttasíða Eysteins</h1>
</header>
  
<nav>
  <ul style="list-style-type:disc">
<li><a href="/frett/0">Stórhríð og stormur í vændum</a></li><br>
<li><a href="/frett/1">Ók á mann og sparkaði í hann</a></li><br>
<li><a href="/frett/2">Hér er pláss fyr­ir miklu fleiri</a></li><br>
  </ul>
</nav>

<article>
% nr = int(id)
{{f[nr][0]}}<br>
{{f[nr][1]}}<br>
{{f[nr][2]}}

<div class="container">
</div>


</article>

<footer>Fréttasíða</footer>

</div>


</body>
</html>