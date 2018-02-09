'use strict';

var app = angular.module('myApp', []);

app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

app.controller("homeCtrl", function($scope, $http, $interval) {
		
	function countFaces(){
		$http.get("/on_load").then(function(response){
			$scope.faces = response.data.faces;
			console.log($scope.faces);
			countFaces();
		});
	};

	countFaces();
	
});