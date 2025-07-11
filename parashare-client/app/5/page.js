'use client'
import React from 'react'
import Head from 'next/head'


const TakeUmbrellaScreen = (props) => {
  return (
    <>
      <div className="take-umbrella-screen-container">
        <Head>
          <title>exported project</title>
        </Head>
        <div className="take-umbrella-screen-take-umbrella-screen">
          <div className="take-umbrella-screen-take-content">
            <div className="take-umbrella-screen-instructions-card">
              <span className="take-umbrella-screen-text1">貸出完了！</span>
              <div className="take-umbrella-screen-card-content">
                <span className="take-umbrella-screen-text2">
                  傘をお取りください
                </span>
                <span className="take-umbrella-screen-text3">
                  返却期限：3日以内
                </span>
                <div className="take-umbrella-screen-point-info">
                  <span className="take-umbrella-screen-text4">
                    使用ポイント：5P
                  </span>
                  <span className="take-umbrella-screen-text5">
                    残りポイント：7P
                  </span>
                </div>
              </div>
            </div>
            <div className="take-umbrella-screen-success-animation"></div>
            <div className="take-umbrella-screen-umbrella-container">
              <img
                src="/external/umbrella_green.svg"
                alt="Umbrella5735"
                className="take-umbrella-screen-umbrella"
              />
            </div>
          </div>
        </div>
      </div>
      <style jsx>
        {`
          .take-umbrella-screen-container {
            width: 100%;
            display: flex;
            overflow: auto;
            min-height: 100vh;
            align-items: center;
            flex-direction: column;
          }
          .take-umbrella-screen-take-umbrella-screen {
            width: 100%;
            height: auto;
            display: flex;
            padding: 40px;
            align-items: center;
            flex-shrink: 0;
            flex-direction: column;
            justify-content: center;
            background-color: rgba(40, 167, 69, 1);
          }
          .take-umbrella-screen-take-content {
            gap: 40px;
            width: 600px;
            height: 540px;
            display: flex;
            position: relative;
            align-items: center;
            flex-shrink: 0;
          }
          .take-umbrella-screen-instructions-card {
            top: 224px;
            left: 36px;
            width: 540px;
            height: 312px;
            display: flex;
            padding: 32px;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 24px;
            justify-content: center;
            background-color: rgba(255, 255, 255, 1);
          }
          .take-umbrella-screen-text1 {
            top: 35px;
            left: 190px;
            color: rgba(40, 167, 69, 1);
            height: auto;
            position: absolute;
            font-size: 32px;
            font-style: Bold;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 700;
            line-height: 43.20000076293945px;
            font-stretch: normal;
            text-decoration: none;
          }
          .take-umbrella-screen-card-content {
            gap: 24px;
            top: 106px;
            left: 162px;
            width: 216px;
            height: 147px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .take-umbrella-screen-text2 {
            color: rgba(51, 51, 51, 1);
            height: auto;
            top: 0;
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
          .take-umbrella-screen-text3 {
            top: 53px;
            left: 22px;
            color: rgba(102, 102, 102, 1);
            height: auto;
            position: absolute;
            font-size: 20px;
            font-style: Medium;
            text-align: center;
            font-family: Noto Sans JP;
            font-weight: 500;
            line-height: 21.600000381469727px;
            font-stretch: normal;
            text-decoration: none;
          }
          .take-umbrella-screen-point-info {
            gap: 8px;
            top: 99px;
            left: 42.5px;
            width: 131px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-direction: column;
          }
          .take-umbrella-screen-text4 {
            color: rgba(153, 153, 153, 1);
            height: auto;
            font-size: 16px;
            font-style: Regular;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 400;
            line-height: 19.200000762939453px;
            font-stretch: normal;
            text-decoration: none;
          }
          .take-umbrella-screen-text5 {
            color: rgba(153, 153, 153, 1);
            height: auto;
            font-size: 16px;
            font-style: Regular;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 400;
            line-height: 19.200000762939453px;
            font-stretch: normal;
            text-decoration: none;
          }
          .take-umbrella-screen-success-animation {
            gap: 32px;
            top: 180px;
            left: 408px;
            width: 180px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-direction: column;
          }
          .take-umbrella-screen-umbrella-container {
            top: 33px;
            left: 230px;
            width: 140px;
            height: 140px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 70px;
            flex-direction: column;
            justify-content: center;
            background-color: rgba(255, 255, 255, 1);
          }
          .take-umbrella-screen-umbrella {
            width: 70px;
            height: 70px;
          }
        `}
      </style>
    </>
  )
}

export default TakeUmbrellaScreen
