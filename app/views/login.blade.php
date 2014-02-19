<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Laravel PHP Framework</title>
	<!--<link rel="stylesheet" href="login.css">-->
	{{ HTML::style('login.css'); }}
</head>
<body>
	<div id="fb-root"></div>
	<fb:login-button show-faces="true" width="200" max-rows="1"></fb:login-button>
	<!-- <script src="login.js" ></script> -->
	{{ HTML::script('login.js') }}
</body>
</html>
