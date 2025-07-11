'use client'
import React, { useEffect, useState } from 'react'
import Head from 'next/head'
import { useRouter } from "next/navigation";

const CompletionScreen = (props) => {
  const router = useRouter();
  const [countdown, setCountdown] = useState(5);

  useEffect(() => {
    // カウントダウンタイマー
    const timer = setInterval(() => {
      setCountdown((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          router.push('/1'); // 最初の画面に戻る
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    // コンポーネントがアンマウントされる時にタイマーをクリア
    return () => clearInterval(timer);
  }, [router]);
  return (
    <>
      <div className="completion-screen-container">
        <Head>
          <title>exported project</title>
        </Head>
        <div className="completion-screen-completion-screen">
          <div className="completion-screen-completion-content">
            <div className="completion-screen-success-icon">
              <img
                src="/external/circle-check-big.svg"
                alt="CheckCircle5746"
                className="completion-screen-check-circle"
              />
            </div>
            <div className="completion-screen-completion-card">
              <div className="completion-screen-card-content">
                <span className="completion-screen-text1">
                  ご利用ありがとうございました
                </span>
                <div className="completion-screen-time-info">
                  <div className="completion-screen-return-date-card">
                    <span className="completion-screen-text2">返却期限</span>
                    <span className="completion-screen-text3">
                      2024年12月18日 17:00
                    </span>
                  </div>
                </div>
                <div className="completion-screen-reminder">
                  <span className="completion-screen-text4">
                    期限内の返却でポイントが回復します
                  </span>
                </div>
                <span className="completion-screen-text5">
                  遅延すると追加ポイントが必要になります
                </span>
              </div>
              <span className="completion-screen-text6">
                {countdown}秒後に最初の画面に戻ります...
              </span>
            </div>
          </div>
        </div>
      </div>
      <style jsx>
        {`
          .completion-screen-container {
            width: 100%;
            display: flex;
            overflow: auto;
            min-height: 100vh;
            align-items: center;
            flex-direction: column;
          }
          .completion-screen-completion-screen {
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
          .completion-screen-completion-content {
            gap: 32px;
            width: 700px;
            height: 532px;
            display: flex;
            position: relative;
            align-items: center;
            flex-shrink: 0;
          }
          .completion-screen-success-icon {
            top: 0px;
            left: 300px;
            width: 120px;
            height: 120px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 60px;
            flex-direction: column;
            justify-content: center;
            background-color: rgba(40, 167, 69, 1);
          }
          .completion-screen-check-circle {
            width: 50px;
            height: 50px;
          }
          .completion-screen-completion-card {
            top: 164px;
            left: 50px;
            width: 600px;
            height: 368px;
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
          .completion-screen-card-content {
            gap: 24px;
            top: 61px;
            left: 100px;
            width: 400px;
            height: 247px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .completion-screen-text1 {
            left: -20px;
            top: -20px;
            color: rgba(184, 28, 34, 1);
            height: auto;
            position: absolute;
            font-size: 32px;
            font-style: Bold;
            text-align: center;
            font-family: Noto Sans JP;
            white-space: nowrap;
            font-weight: 700;
            line-height: 28.799999237060547px;
            font-stretch: normal;
            text-decoration: none;
          }
          .completion-screen-time-info {
            gap: 20px;
            top: 53.5px;
            left: 0px;
            width: 400px;
            height: 80px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .completion-screen-return-date-card {
            top: 0px;
            left: -32px;
            width: 464px;
            height: 101px;
            display: flex;
            padding: 16px;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 16px;
            justify-content: center;
            background-color: rgba(240, 249, 255, 1);
          }
          .completion-screen-text2 {
            top: 12px;
            left: 192px;
            color: rgba(102, 102, 102, 1);
            height: auto;
            position: absolute;
            font-size: 20px;
            font-style: Medium;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 500;
            line-height: 19.200000762939453px;
            font-stretch: normal;
            text-decoration: none;
          }
          .completion-screen-text3 {
            top: 51px;
            left: 101px;
            color: rgba(0, 91, 172, 1);
            height: auto;
            position: absolute;
            font-size: 24px;
            font-style: Black;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 900;
            line-height: 24px;
            font-stretch: normal;
            text-decoration: none;
          }
          .completion-screen-reminder {
            gap: 12px;
            top: 171.5px;
            left: 64px;
            width: 272px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-direction: column;
          }
          .completion-screen-text4 {
            color: rgba(40, 167, 69, 1);
            height: auto;
            font-size: 16px;
            font-style: Medium;
            text-align: center;
            font-family: Noto Sans JP;
            font-weight: 500;
            line-height: 19.200000762939453px;
            font-stretch: normal;
            text-decoration: none;
          }
          .completion-screen-text5 {
            top: 206.5px;
            left: 67px;
            color: rgba(230, 0, 32, 1);
            height: auto;
            position: absolute;
            font-size: 14px;
            font-style: Regular;
            text-align: center;
            font-family: Noto Sans JP;
            font-weight: 400;
            line-height: 16.799999237060547px;
            font-stretch: normal;
            text-decoration: none;
          }
          .completion-screen-text6 {
            top: 308px;
            left: 199px;
            color: rgba(153, 153, 153, 1);
            height: auto;
            position: absolute;
            font-size: 14px;
            font-style: Regular;
            text-align: center;
            font-family: Noto Sans JP;
            font-weight: 400;
            line-height: 16.799999237060547px;
            font-stretch: normal;
            text-decoration: none;
          }
        `}
      </style>
    </>
  )
}

export default CompletionScreen
