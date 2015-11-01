routerApp.controller('signupCtrl',function($scope,$http)
{
	$scope.create_user = function()
	{
		var promise = $http.post("http://localhost:3000/users", { 
			"user": {
					"email":$scope.user_email,
					"password":$scope.user_password,
					"username":$scope.user_name
				}
		});

		promise.success(function(data,status,header,config) {
			console.log("User Joined");
		});
		promise.error(function(a,b,c){console.log(a,b,c)});
	};	
});