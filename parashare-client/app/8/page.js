'use client'
import React from 'react'
import Head from 'next/head'
import { useRouter } from "next/navigation";

const AuthErrorScreen = (props) => {
  const router = useRouter();

  const handleRetry = () => {
    console.log('再試行ボタンが押されました。/1ページに遷移します...');
    router.push('/1');
  };
  return (
    <>
      <div className="auth-error-screen-container">
        <Head>
          <title>exported project</title>
        </Head>
        <div className="auth-error-screen-auth-error-screen">
          <div className="auth-error-screen-error-icon">
            <img
              src="/external/triangle-alert.svg"
              alt="AlertTriangle5738"
              className="auth-error-screen-alert-triangle"
            />
          </div>
          <div className="auth-error-screen-error-content">
            <div className="auth-error-screen-error-card">
              <div className="auth-error-screen-card-content">
                <span className="auth-error-screen-text1">認証エラー</span>
                <div className="auth-error-screen-error-message">
                  <span className="auth-error-screen-text2">
                    学生証を確認できませんでした
                  </span>
                </div>
                <span className="auth-error-screen-text3">
                  もう一度お試しください
                </span>
                <button className="auth-error-screen-retry-button" onClick={handleRetry}>
                  <div className="auth-error-screen-button-content">
                    <img
                      src="/external/refresh-cw.svg"
                      alt="RefreshCw5741"
                      className="auth-error-screen-refresh-cw"
                    />
                    <span className="auth-error-screen-text4">再試行</span>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <style jsx>
        {`
          .auth-error-screen-container {
            width: 100%;
            display: flex;
            overflow: auto;
            min-height: 100vh;
            align-items: center;
            flex-direction: column;
          }
          .auth-error-screen-auth-error-screen {
            width: 100%;
            height: 600px;
            display: flex;
            position: relative;
            align-items: center;
            flex-shrink: 0;
            justify-content: center;
            background-color: rgba(230, 0, 32, 1);
          }
          .auth-error-screen-error-icon {
            top: 62px;
            width: 140px;
            height: 140px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 70px;
            justify-content: center;
            background-color: rgba(255, 255, 255, 1);
          }
          .auth-error-screen-alert-triangle {
            top: 40px;
            left: 40px;
            width: 60px;
            height: 60px;
            position: absolute;
          }
          .auth-error-screen-error-content {
            gap: 40px;
            top: 285px;
            width: 600px;
            height: 328px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .auth-error-screen-error-card {
            gap: 37px;
            top: -32px;
            left: 60px;
            width: 480px;
            height: 312px;
            display: flex;
            padding: 58px 40px 40px;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 24px;
            justify-content: center;
            background-color: rgba(255, 255, 255, 1);
          }
          .auth-error-screen-card-content {
            gap: 32px;
            top: 38px;
            left: 100.5px;
            width: 279px;
            height: 222px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .auth-error-screen-text1 {
            left: 67.5px;
            top: 0;
            color: rgba(230, 0, 32, 1);
            height: auto;
            position: absolute;
            font-size: 32px;
            font-style: Bold;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 700;
            line-height: 33.599998474121094px;
            font-stretch: normal;
            text-decoration: none;
          }
          .auth-error-screen-error-message {
            gap: 16px;
            top: 66px;
            left: 0px;
            width: 279px;
            height: 60px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .auth-error-screen-text2 {
            top: 10px;
            left: -0.5px;
            color: rgba(51, 51, 51, 1);
            height: auto;
            position: absolute;
            font-size: 20px;
            font-style: Black;
            text-align: center;
            font-family: Noto Sans JP;
            font-weight: 900;
            line-height: 24px;
            font-stretch: normal;
            text-decoration: none;
          }
          .auth-error-screen-text3 {
            top: 126px;
            left: 51.5px;
            color: rgba(102, 102, 102, 1);
            height: auto;
            position: absolute;
            font-size: 16px;
            font-style: Medium;
            text-align: center;
            font-family: Noto Sans JP;
            font-weight: 500;
            line-height: 19.200000762939453px;
            font-stretch: normal;
            text-decoration: none;
          }
          .auth-error-screen-retry-button {
            top: 190px;
            left: 19.5px;
            width: 240px;
            height: 64px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 32px;
            justify-content: center;
            background-color: rgba(230, 0, 32, 1);
            border: none;
            cursor: pointer;
            transition: background-color 0.2s ease;
          }
          .auth-error-screen-retry-button:hover {
            background-color: rgba(200, 0, 28, 1);
          }
          .auth-error-screen-button-content {
            gap: 12px;
            top: 21px;
            left: 77px;
            width: 86px;
            display: flex;
            position: absolute;
            align-items: center;
            pointer-events: none;
          }
          .auth-error-screen-refresh-cw {
            width: 20px;
            height: 20px;
          }
          .auth-error-screen-text4 {
            color: rgba(255, 255, 255, 1);
            height: auto;
            font-size: 18px;
            font-style: Black;
            text-align: left;
            font-family: Noto Sans JP;
            white-space: nowrap;
            font-weight: 900;
            line-height: 21.600000381469727px;
            font-stretch: normal;
            text-decoration: none;
          }
        `}
      </style>
    </>
  )
}

export default AuthErrorScreen
