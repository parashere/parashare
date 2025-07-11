'use client'
import React from 'react'
import Head from 'next/head'
import { useRouter } from "next/navigation";

const NoUmbrellaErrorScreen = (props) => {
  const router = useRouter();
  
  const handleRetry = () => {
    console.log('再試行ボタンが押されました。/1ページに遷移します...');
    router.push('/1');
  };
  return (
    <>
      <div className="no-umbrella-error-screen-container">
        <Head>
          <title>exported project</title>
        </Head>
        <div className="no-umbrella-error-screen-no-umbrella-error-screen">
          <div className="no-umbrella-error-screen-warning-icon">
            <img
              src="/external/circle-alert.svg"
              alt="AlertCircle5743"
              className="no-umbrella-error-screen-alert-circle"
            />
          </div>
          <div className="no-umbrella-error-screen-warning-content">
            <div className="no-umbrella-error-screen-warning-card">
              <div className="no-umbrella-error-screen-card-content">
                <span className="no-umbrella-error-screen-text1">傘不足</span>
                <div className="no-umbrella-error-screen-warning-message">
                  <span className="no-umbrella-error-screen-text2">
                    他の学生の返却をお待ちください
                  </span>
                </div>
                <span className="no-umbrella-error-screen-text3">
                  現在傘がありません
                </span>
                <div className="no-umbrella-error-screen-return-info">
                  <span className="no-umbrella-error-screen-text4">
                    返却場所のご案内
                  </span>
                  <span className="no-umbrella-error-screen-text5">
                    図書館前・学生会館・各学部棟入口
                  </span>
                </div>
                <button className="no-umbrella-error-screen-retry-button" onClick={handleRetry}>
                  <div className="no-umbrella-error-screen-button-content">
                    <span className="no-umbrella-error-screen-text6">戻る</span>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <style jsx>
        {`
          .no-umbrella-error-screen-container {
            width: 100%;
            display: flex;
            overflow: auto;
            min-height: 100vh;
            align-items: center;
            flex-direction: column;
          }
          .no-umbrella-error-screen-no-umbrella-error-screen {
            width: 100%;
            height: 600px;
            display: flex;
            position: relative;
            align-items: center;
            flex-shrink: 0;
            justify-content: center;
            background-color: rgba(255, 193, 7, 1);
          }
          .no-umbrella-error-screen-warning-icon {
            top: 50px;
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
          .no-umbrella-error-screen-alert-circle {
            top: 40px;
            left: 40px;
            width: 60px;
            height: 60px;
            position: absolute;
          }
          .no-umbrella-error-screen-warning-content {
            gap: 40px;
            top: 225px;
            width: 600px;
            height: 360px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .no-umbrella-error-screen-warning-card {
            top: 13px;
            left: 40px;
            width: 520px;
            height: 334px;
            display: flex;
            padding: 40px;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 24px;
            justify-content: center;
            background-color: rgba(255, 255, 255, 1);
          }
          .no-umbrella-error-screen-card-content {
            gap: 24px;
            top: 46px;
            left: 140px;
            width: 240px;
            height: 268px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .no-umbrella-error-screen-text1 {
            top: -20px;
            left: 64px;
            color: rgba(255, 193, 7, 1);
            height: auto;
            position: absolute;
            font-size: 36px;
            font-style: Bold;
            text-align: left;
            font-family: Noto Sans JP;
            white-space: nowrap;
            font-weight: 700;
            line-height: 33.599998474121094px;
            font-stretch: normal;
            text-decoration: none;
          }
          .no-umbrella-error-screen-warning-message {
            gap: 16px;
            top: 58px;
            left: 0px;
            width: 240px;
            height: 60px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .no-umbrella-error-screen-text2 {
            top: 30px;
            left: -30px;
            color: rgba(102, 102, 102, 1);
            height: auto;
            position: absolute;
            font-size: 20px;
            font-style: Medium;
            text-align: center;
            font-family: Noto Sans JP;
            white-space: nowrap;
            font-weight: 500;
            line-height: 19.200000762939453px;
            font-stretch: normal;
            text-decoration: none;
          }
          .no-umbrella-error-screen-text3 {
            top: 46px;
            left: 10px;
            color: rgba(51, 51, 51, 1);
            height: auto;
            position: absolute;
            font-size: 24px;
            font-style: Black;
            text-align: center;
            font-family: Noto Sans JP;
            font-weight: 900;
            line-height: 24px;
            font-stretch: normal;
            text-decoration: none;
          }
          .no-umbrella-error-screen-return-info {
            gap: 12px;
            top: 142px;
            left: 8px;
            width: 224px;
            height: 46px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .no-umbrella-error-screen-text4 {
            top: -8px;
            left: 48px;
            color: rgba(153, 153, 153, 1);
            height: auto;
            position: absolute;
            font-size: 16px;
            font-style: Regular;
            text-align: center;
            font-family: Noto Sans JP;
            font-weight: 400;
            line-height: 16.799999237060547px;
            font-stretch: normal;
            text-decoration: none;
          }
          .no-umbrella-error-screen-text5 {
            top: 14px;
            left: -16px;
            color: rgba(153, 153, 153, 1);
            height: auto;
            position: absolute;
            font-size: 16px;
            font-style: Regular;
            text-align: center;
            font-family: Noto Sans JP;
            white-space: nowrap;
            font-weight: 400;
            line-height: 16.799999237060547px;
            font-stretch: normal;
            text-decoration: none;
          }
          .no-umbrella-error-screen-retry-button {
            top: 204px;
            left: -2px;
            width: 240px;
            height: 64px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 32px;
            justify-content: center;
            background-color: rgba(255, 193, 7, 1);
            border: none;
            cursor: pointer;
            transition: background-color 0.2s ease;
          }
          .no-umbrella-error-screen-retry-button:hover {
            background-color: rgba(235, 173, 0, 1);
          }
          .no-umbrella-error-screen-button-content {
            gap: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            pointer-events: none;
          }
          .no-umbrella-error-screen-text6 {
            color: rgba(255, 255, 255, 1);
            height: auto;
            font-size: 18px;
            font-style: Black;
            text-align: center;
            font-family: Noto Sans JP;
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

export default NoUmbrellaErrorScreen
