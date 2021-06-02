/* eslint-disable */

import { useState } from "react";
import "./App.css";

function App() {
  let [title, titleRe] = useState(["남자 코트 추천", "두번째 글", "세번째 글"]);
  let [likeNum, likeNumRe] = useState(0);

  // function titleRewrite() {
  //   let newArray = [...title];
  //   newArray[0] = "변경완료";
  //   titleRe(newArray);
  // }

  return (
    <div className="App">
      {/* Nav */}
      <div className="black-nav">
        <div>개발 blog</div>
      </div>

      {/* <button onClick={titleRewrite}>첫번째 글 제목변경</button> */}

      {/* Posts */}
      <ul className="list">
        <h3>
          {title[0]}
          <span
            className="likeBtn"
            onClick={() => {
              likeNumRe(likeNum + 1);
            }}
          >
            👍
          </span>
          {likeNum}
        </h3>
        <p>6월 2일 발행</p>
        <hr />
      </ul>
      <ul className="list">
        <h3> {title[1]} </h3>
        <p>6월 3일 발행</p>
        <hr />
      </ul>
      <ul className="list">
        <h3> {title[2]} </h3>
        <p>6월 4일 발행</p>
        <hr />
      </ul>

      {/* Modal */}
      <Modal></Modal>
    </div>
  );
}

function Modal() {
  return (
    <div className="modal">
      <h2>제목</h2>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  );
}

export default App;
