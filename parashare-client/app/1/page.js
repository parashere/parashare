'use client'
import React, { useEffect } from 'react'
import Head from 'next/head'
import { useRouter } from "next/navigation";

const StandbyScreen = (props) => {
  const router = useRouter();

  useEffect(() => {
    // APIを呼び出してPythonスクリプトを実行
    const runPythonScript = async () => {
      try {
        console.log('Pythonスクリプトを実行中...');
        const response = await fetch('/api/run-python', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
        });

        const data = await response.json();
        
        if (data.success && data.studentID && data.studentID.length > 0) {
          console.log(data.studentID);
          router.push('/2'); // /2ページに移動
        } else {
          console.error('学生番号が取得できませんでした。');
        }
      } catch (error) {
        console.error('APIエラー:', error);
      }
    };

    runPythonScript();
  }, [router]);
  return (
    <>
      <div className="standby-screen-container">
        <Head>
          <title>exported project</title>
        </Head>
        <div className="standby-screen-standby-screen">
          <div className="standby-screen-main-content">
            <div className="standby-screen-logo-section">
              <div className="standby-screen-logo-circle">
                <img
                  src="/external/umbrella.svg"
                  alt="Umbrella5722"
                  className="standby-screen-umbrella"
                />
              </div>
            </div>
            <span className="standby-screen-text1">Parashare</span>
            <div className="standby-screen-card-container">
              <div className="standby-screen-card-content">
                <div className="standby-screen-student-card-icon">
                  <img
                    src="/external/credit-card.svg"
                    alt="CreditCard5725"
                    className="standby-screen-credit-card"
                  />
                </div>
                <span className="standby-screen-text2">
                  学生証をタップしてください
                </span>
                <div className="standby-screen-touch-hint">
                  <span className="standby-screen-text3">ここにタッチ</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <style jsx>
        {`
          .standby-screen-container {
            width: 100%;
            display: flex;
            overflow: auto;
            min-height: 100vh;
            align-items: center;
            flex-direction: column;
          }
          .standby-screen-standby-screen {
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
          .standby-screen-main-content {
            gap: 48px;
            width: 600px;
            height: 568px;
            display: flex;
            position: relative;
            align-items: center;
            flex-shrink: 0;
          }
          .standby-screen-logo-section {
            gap: 32px;
            top: 0px;
            left: 201px;
            width: 198px;
            height: 240px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .standby-screen-logo-circle {
            top: 15px;
            left: 19px;
            width: 160px;
            height: 160px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 80px;
            flex-direction: column;
            justify-content: center;
            background-color: rgba(184, 28, 34, 1);
          }
          .standby-screen-umbrella {
            width: 64px;
            height: 64px;
          }
          .standby-screen-text1 {
            top: 216px;
            left: 147px;
            color: rgba(184, 28, 34, 1);
            height: auto;
            position: absolute;
            font-size: 64px;
            font-style: Bold;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 700;
            line-height: 48px;
            font-stretch: normal;
            text-decoration: none;
          }
          .standby-screen-card-container {
            top: 300px;
            left: 60px;
            width: 480px;
            height: 252px;
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
          .standby-screen-card-content {
            gap: 32px;
            top: 27.5px;
            left: 84.5px;
            width: 311px;
            height: 225px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .standby-screen-student-card-icon {
            top: 0px;
            left: 115.5px;
            width: 80px;
            height: 80px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 16px;
            flex-direction: column;
            justify-content: center;
            background-color: rgba(230, 0, 32, 1);
          }
          .standby-screen-credit-card {
            width: 40px;
            height: 40px;
          }
          .standby-screen-text2 {
            top: 112px;
            color: rgba(51, 51, 51, 1);
            height: auto;
            position: absolute;
            font-size: 24px;
            font-style: Black;
            text-align: center;
            font-family: Noto Sans JP;
            font-weight: 900;
            line-height: 28.799999237060547px;
            font-stretch: normal;
            text-decoration: none;
          }
          .standby-screen-touch-hint {
            gap: 8px;
            top: 152.5px;
            left: 107.5px;
            width: 96px;
            height: 52px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .standby-screen-text3 {
            top: 32px;
            color: rgba(153, 153, 153, 1);
            height: auto;
            position: absolute;
            font-size: 16px;
            font-style: Regular;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 400;
            line-height: 19.200000762939453px;
            font-stretch: normal;
            text-decoration: none;
          }
        `}
      </style>
    </>
  )
}

export default StandbyScreen
