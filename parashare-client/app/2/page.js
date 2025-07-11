'use client'
import React from 'react'
import Head from 'next/head'
import { useRouter, useSearchParams } from "next/navigation";

const LoginSuccessScreen = (props) => {
  const router = useRouter();
  const searchParams = useSearchParams();
  const studentID = searchParams.get('studentID') || 't323'; // デフォルト値を設定
  const handleRetry = () => {
    console.log('再試行ボタンが押されました。/1ページに遷移します...');
    router.push('/5');
  };
  return (
    <>
      <div className="login-success-screen-container">
        <Head>
          <title>exported project</title>
        </Head>
        <div className="login-success-screen-login-success-screen">
          <div className="login-success-screen-success-content">
            <div className="login-success-screen-success-icon">
              <img
                src="/external/check.svg"
                alt="Check5727"
                className="login-success-screen-check"
              />
            </div>
            <div className="login-success-screen-success-card">
              <div className="login-success-screen-card-content">
                <div className="login-success-screen-student-info">
                  <span className="login-success-screen-text1">学生番号</span>
                </div>
                <span className="login-success-screen-text2">{studentID}</span>
                <button className="login-success-screen-next-button" onClick={handleRetry}>
                  <span className="login-success-screen-text3">次へ進む</span>
                </button>
              </div>
            </div>
            <span className="login-success-screen-text4">認証成功</span>
          </div>
        </div>
      </div>
      <style jsx>
        {`
          .login-success-screen-container {
            width: 100%;
            display: flex;
            overflow: auto;
            min-height: 100vh;
            align-items: center;
            flex-direction: column;
          }
          .login-success-screen-login-success-screen {
            width: 100%;
            height: auto;
            display: flex;
            padding: 40px;
            align-items: center;
            flex-shrink: 0;
            flex-direction: column;
            justify-content: center;
            background-color: rgba(248, 249, 250, 1);
          }
          .login-success-screen-success-content {
            gap: 40px;
            width: 600px;
            height: 480px;
            display: flex;
            position: relative;
            align-items: center;
            flex-shrink: 0;
          }
          .login-success-screen-success-icon {
            top: -23px;
            left: 220px;
            width: 160px;
            height: 160px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 80px;
            justify-content: center;
            background-color: rgba(40, 167, 69, 1);
          }
          .login-success-screen-check {
            top: 50px;
            left: 50px;
            width: 60px;
            height: 60px;
            position: absolute;
          }
          .login-success-screen-success-card {
            top: 253px;
            left: 30px;
            width: 540px;
            height: 257px;
            display: flex;
            padding: 40px;
            position: absolute;
            box-shadow: 0px 4px 20px 0px rgba(0, 0, 0, 0.062745101749897);
            align-items: center;
            flex-shrink: 0;
            border-radius: 24px;
            justify-content: center;
            background-color: rgba(255, 255, 255, 1);
          }
          .login-success-screen-card-content {
            gap: 32px;
            top: -10px;
            left: 110px;
            width: 320px;
            height: 244px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .login-success-screen-student-info {
            gap: 16px;
            top: 40px;
            left: 53px;
            width: 213px;
            height: 82px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .login-success-screen-text1 {
            left: 59px;
            color: rgba(102, 102, 102, 1);
            height: auto;
            position: absolute;
            font-size: 24px;
            font-style: Medium;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 500;
            line-height: 21.600000381469727px;
            font-stretch: normal;
            text-decoration: none;
          }
          .login-success-screen-text2 {
            top: 100px;
            left: 18px;
            color: rgba(184, 28, 34, 1);
            height: auto;
            position: absolute;
            font-size: 48px;
            font-style: Bold;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 700;
            line-height: 43.20000076293945px;
            font-stretch: normal;
            text-decoration: none;
          }
          .login-success-screen-next-button {
            top: 180px;
            left: 0px;
            width: 320px;
            height: 64px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 32px;
            flex-direction: column;
            justify-content: center;
            background-color: rgba(0, 91, 172, 1);
            border: none;
            cursor: pointer;
          }
          .login-success-screen-text3 {
            color: rgba(255, 255, 255, 1);
            height: auto;
            font-size: 20px;
            font-style: Black;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 900;
            line-height: 24px;
            font-stretch: normal;
            text-decoration: none;
          }
          .login-success-screen-text4 {
            top: 176px;
            left: 220px;
            color: rgba(40, 167, 69, 1);
            height: auto;
            position: absolute;
            font-size: 40px;
            font-style: Bold;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 700;
            line-height: 33.599998474121094px;
            font-stretch: normal;
            text-decoration: none;
          }
        `}
      </style>
    </>
  )
}

export default LoginSuccessScreen
