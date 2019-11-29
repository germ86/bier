<?php
	session_start();
?>
<!DOCTYPE HTML>
<html>
	<head>
		
		<!-- TITLE -->
		<title>
			Fabio-Schmeil.de
		</title>
		
		<!-- META INFORMATIONEN -->
		<meta charset="UTF-8">
		<meta http-equiv="content-type" content="text/html; charset=UTF-8">
		<meta http-equiv="Content-Style-Type" content="text/css">
		<meta http-equiv="content-language" content="de">
		<meta name='keywords' lang='de'  content='globukalypse, bot, bier, bierforce, twankenhaus, opensource, openscience, twitter, api, facebook, development, AI, KI'>
		<meta name='descripton' content='Der Bierbot ist ein Projekt was im Rahmen der Globukalypse entsteht. Es soll als Projekt dazu dienen sich mit App entwicklung und AI zu beschäftigen'>
		<meta name='author' content='Fabio Schmeil'>
		<meta name='title' content='Fabio-Schmeil.de'>
		<meta name='publisher' content='Fabio Schmeil'>
		<meta name='date' content='2019-11-27'>	
		<meta name='type' content='text'>
		<meta name='format' content='text/html'>
		<meta name='robots' content='all'>
		<!-- STYLESHEET -->
		<link type='text/css' rel="stylesheet" href="css/main.css">
	
	</head>
	<body>
		<header>
			<h1>
				B.I.E.R
			</h1>
		</header>
		<nav>
			<menu>
				<ul>
				<li>
					<a href="index.php?id=10">Home |</a>
				</li>
				<li>
					<a href="index.php?id=1337">Login |</a>
				</li>
				<li>
					<a href="index.php?id=30">Nutzungsbedingungen |</a>
				</li>
				<li>
					<a href="index.php?id=40">Datenschutzerklärung</a>
			<!--
				<li>
					<a href="index.php?id=30">Referenzen |</a>
				</li>
				<li>
					<a href="index.php?id=40">Links |</a>
				</li

				<li>
					<a href="index.php?id=50">Impressum / Kontakt</a>
				</li>
				-->
		</ul>	
		</menu>
		</nav>
		<div id='content'>
		<article>
			<?php
				$id = $_GET['id'];
				switch($id) {
					case 10: 
						include "php/inc/home.inc.php";
						break;
					
				//	case 20: 
				//		include "php/inc/login.inc.php";
				//		break;
					
					case 30: 
						include "php/inc/terms.inc.php";
						break;
					case 40: 
						include "php/inc/policy.inc.php";
						break;
					case 50: 
						include "php/inc/kontakt.inc.php";
						break;
					case 1337: 
						include "php/inc/login.inc.php";
						break;
					case 666: 
						include "php/inc/archive.inc.php";
						break;
					default:
						include "php/inc/home.inc.php";
				}
			?>	
		</article>
		</div>
		<footer>
			<menu>
					<a href="index.php?id=40">Impressum / Kontakt </a>
			</menu>
		</footer>
	</body>
</html>
