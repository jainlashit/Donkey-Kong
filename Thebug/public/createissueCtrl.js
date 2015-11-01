routerApp.controller('createissueCtrl',function($scope,$http)
{
	$scope.create_issue = function()
	{
		var promise = $http.post("http://localhost:3000/issues/", {
			"issue": {
					"project":$scope.project_name1,
					"tag":$scope.issue_tag1
				}
		});

		promise.success(function(data,status,header,config) {
			console.log("Issue Created");
		});
		promise.error(function(a,b,c){console.log(a,b,c)});
	};	
});