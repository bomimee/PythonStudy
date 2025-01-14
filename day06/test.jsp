<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
                <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<c:set var="path" value="${pageContext.request.contextPath}" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>1:1문의</title>
<link rel="stylesheet" href="${path}/resources/public/css/bm/inquiry_form.css">

<link href="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-lite.min.css" rel="stylesheet">
<script defer src="${path}/resources/public/js/bm/lang/summernote-ko-KR.js"></script>
<script defer src="${path}/resources/public/js/bm/summernote-lite.js"></script>
  <script defer src="${path}/resources/public/js/bm/my_menu.js"></script>
 <script>
      function handleModiUp(qna_idx) {
        href.location = "QnaUpdate.do";
      }
    </script>
</head>
<body>
 <div class="form_container">
  <h1 class="inquiry_title">1:1문의</h1>
  <form class="form_inquiry" method="post" enctype="multipart/form-data">
    <div class="title_box">
          <input
            type="text"
            placeholder="글제목"
            class="input_title"
            name="qna_title"
            value="${qvo.qna_title}"
          />
        </div>
        <textarea
          class="text_area summernote"
          id="summernote"
          name="qna_content"
        >
          ${qvo.qna_content}
        </textarea>
      <div class="form_btn">
       <input
              type="hidden"
              id="memberIdx"
              name="member_idx"
              value="${qvo.member_idx}"
            />
     <input
              type="hidden"
              id="memberIdx"
              name="member_idx"
              value="${qvo.qna_idx}"
            />
        <button class="btn btn-modi" onclick="handleModiUp()">저장 </button>
        <button class="btn btn-cancel">취소</button>
      </div>
    </div>
  </form>
  </div>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js" crossorigin="anonymous"></script>
   <script>
    $(document).ready(function() {
    	$('.summernote').summernote({

    	    lang : 'ko-KR',
        	height : 300,
        	focus : true,
    	 
    	    })
    	});
 
   </script>
       <script>
        var socket = new SockJS('/ws');

        var stompClient = Stomp.over(socket);

        stompClient.connect({}, function (frame) {
            stompClient.subscribe('/topic/public', function (response) {
                showMessage(JSON.parse(response.body).content);
            });
        });

        function sendMessage() {
            var messageInput = document.getElementById("messageInput");
            stompClient.send("/app/chat.sendMessage", {}, JSON.stringify({ 'content': messageInput.value }));
            messageInput.value = '';
        }

        function showMessage(message) {
            var chatDiv = document.getElementById("chat");
            var p = document.createElement("p");
            p.appendChild(document.createTextNode(message));
            chatDiv.appendChild(p);
        }
    </script>
</body>
</html>