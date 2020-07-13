'use strict'
var son='b'

//显示bootstrap4提示框效果
$('[data-toggle="tooltip"]').tooltip()

// using jQuery
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
	// 这些HTTP方法不要求CSRF包含
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
	beforeSend: function(xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});

$('.badge-warning').hover(
	function(){$(this).children('i').removeClass('m-1').addClass('mx-2 my-1');$(this).addClass('shadow')},
	function(){$(this).children('i').removeClass('mx-2 my-1').addClass('m-1');$(this).removeClass('shadow')}
)

$('#motorcycle').click(
	function(){son='b';getRainbowFart()}
)

$('#bicycle').click(
	function(){son='z';getRainbowFart()}
)

$('#next_Btn').click(
	function(){getRainbowFart()}
)

$('#copy_Btn').click(
	function(){
		$('#show_Text').select()
		if (document.execCommand('copy',false,null)) {
			$('#alert_Info').html('复制成功o(*￣▽￣*)ブ！可以发wb咯o(*￣▽￣*)ブ')
			$('#alert_Info').addClass('alert-success')
			$('#alert_Info').collapse('show')
			setTimeout("$('#alert_Info').html('');$('#alert_Info').removeClass('alert-success');$('#alert_Info').collapse('hide')",3000)
		}
		else{
			$('#alert_Info').html('复制失败(；′⌒`)！试试手动复制或联系开发者/(ㄒoㄒ)/~~')
			$('#alert_Info').addClass('alert-danger')
			$('#alert_Info').collapse('show')
			setTimeout("$('#alert_Info').html('');$('#alert_Info').removeClass('alert-danger');$('#alert_Info').collapse('hide')",3000)
		}
	}
)

$('#analyze_Btn').click(
	function(){
		if ($('#emotion_Analyze').val().indexOf('王一博')==-1&&$('#emotion_Analyze').val().indexOf('肖战')==-1) {
			alert('没有啵比赞比？o_o ....')
		}
		else{
			$.ajax({
				url:'analyzeText',
				type:'POST',
				contentType:'json',
				data:JSON.stringify({
					'text':$('#emotion_Analyze').val(),
				}),
				success:function(result){
					result=JSON.parse(result)
					if (result['score']>0.7) {
						if ($('#emotion_Analyze').val().indexOf('王一博')!=-1) {
							$('#emotion_Result').html(String(Number(result['score'])*100)+'分<i class="far fa-kiss-wink-heart fa-2x"></i>啵比最喜欢你了')
						}
						else if($('#emotion_Analyze').val().indexOf('肖战')!=-1){
							$('#emotion_Result').html(String(Number(result['score'])*100)+'分<i class="far fa-kiss-wink-heart fa-2x"></i>赞比和你世界第一好')
						}
					}
					else if(result['score']>0.3){
						if ($('#emotion_Analyze').val().indexOf('王一博')!=-1) {
							$('#emotion_Result').html(String(Number(result['score'])*100)+'分<<i class="far fa-dizzy fa-2x"></i>啵比想要更多喜欢')
						}
						else if($('#emotion_Analyze').val().indexOf('肖战')!=-1){
							$('#emotion_Result').html(String(Number(result['score'])*100)+'分<i class="far fa-dizzy fa-2x"></i>赞比想要更多喜欢')
						}
					}
					else if(result['score']>0){
						if ($('#emotion_Analyze').val().indexOf('王一博')!=-1) {
							$('#emotion_Result').html(String(Number(result['score'])*100)+'分<i class="far fa-sad-cry fa-2x"></i>妈妈不爱啵比了吗')
						}
						else if($('#emotion_Analyze').val().indexOf('肖战')!=-1){
							$('#emotion_Result').html(String(Number(result['score'])*100)+'分<i class="far fa-sad-cry fa-2x"></i>你不和赞比世界第一好了吗')
						}
					}
				},
				error:function(){
					console.log('分析传递失败')
				},
			})
		}
	}
)

function getRainbowFart()
{
	$.ajax({
		url:'getText',
		type:'POST',
		contentType:'json',
		data:JSON.stringify({
			'son':son,
		}),
		success:function(result){
			$('#show_Text').html(result)
		},
		error:function(){
			console.log('error')
		},
	})
}