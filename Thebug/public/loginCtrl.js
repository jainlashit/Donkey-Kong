routerApp.factory('loginFactory', function ($http,$cookies) {
	var o = {}, baseUrl="http://localhost:3000/token";
    if($cookies.get("Current")==null)
        o.is_loggedin=false;
    else
        o.is_loggedin=true;
	o.login = function(email,password)
	{
        //o.user = email;
		return $http.get(baseUrl + "?email=" + email + "&password=" + password);
	}
    o.logout  = function()
    {
        o.is_loggedin = false;
        $cookies.remove("Current");
    }
 	return o;
});

routerApp.controller('loginCtrl',function($scope,$state,$http,loginFactory,$cookies)
{
    $scope.verify_user  = function(email,password)
    {
        var verify = loginFactory.login(email,password);
        verify.success(function(data) {
            $cookies.put('Current',data.token);
            loginFactory.is_loggedin = true;
            $scope.linker = "http://localhost:3000/index#/signup"
        });
        verify.error(function()
        {
            alert("Incorrect Credentials");
            $scope.linker = "http://localhost:3000/index#/login"
        });
    }
    $scope.hello = function()
    {
        return loginFactory.is_loggedin;
    }
    $scope.remove_user = function()
    {
        loginFactory.logout();
    }
});