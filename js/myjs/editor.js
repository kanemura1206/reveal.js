/*
 * editor is embedded into:
 * <textarea id="editor">hello, world</textarea>
 */
$(function() {
		var editor0 = CodeMirror(function(elt) {
			$("#editor").replaceWith(elt);
			}, {
				value: $("#editor").val(),
				lineNumbers: true,
				mode: "text/x-konoha"
			});
		var editor = CodeMirror(function(elt) {
			$("#editor1").replaceWith(elt);
			}, {
				value: $("#editor1").val(),
				lineNumbers: true,
				mode: "text/x-konoha"
			});
		var libs = {
			setLineColor : function(line,count){
					editor.setLineClass(line - 1,"SGreen");
			},
			setLineError : function(line) {
				editor.setLineClass(line - 1, null);
				editor.setLineClass(line - 1,"SRed");
			},
			setLineClear : function(line) {
				editor.setLineClass(line - 1, null);
			}
		};
	$(".btn").click(function(){
		var data = {};
		$.ajax(
			{
				url:'action.php',
				type:'POST',
				data:data,
				error:function() { $("#log").text("error") },
				complete:function(data) {
					var json = eval(data.responseText);
					$("#log").text(JSON.stringify(json));
					var t = 100;
					var arr = [];
					json.forEach(function(i) {
						if(i.value.count === undefined) {
							i.value["count"] = 1;
							arr.push(i);
							return;
						}
						setTimeout( function() {
							libs.setLineColor(i.value.ScriptLine,i.value.count);
						},t);
						t += 1000;
						});
					arr.forEach(function(i){
						setTimeout( function() {
							libs.setLineError(i.value.ScriptLine);
						},t);
						t += 1000;
						});
					},
				dataType:'json'
			}
		);
	});
});

