'use client'
import React from 'react'
import Head from 'next/head'


const PointsAvailableScreen = (props) => {
  return (
    <>
      <div className="points-available-screen-container">
        <Head>
          <title>exported project</title>
        </Head>
        <div className="points-available-screen-points-available-screen">
          <div className="points-available-screen-points-content">
            <span className="points-available-screen-text1">ポイント確認</span>
            <div className="points-available-screen-points-card">
              <div className="points-available-screen-card-content">
                <span className="points-available-screen-text2">
                  傘の貸出には5ポイント必要です
                </span>
                <div className="points-available-screen-points-display">
                  <div className="points-available-screen-required-card">
                    <span className="points-available-screen-text3">
                      必要ポイント
                    </span>
                    <span className="points-available-screen-text4">5P</span>
                  </div>
                  <div className="points-available-screen-current-card">
                    <span className="points-available-screen-text5">
                      残りポイント
                    </span>
                    <span className="points-available-screen-text6">12P</span>
                  </div>
                </div>
                <div className="points-available-screen-status-badge">
                  <span className="points-available-screen-text7">
                    貸出可能
                  </span>
                </div>
                <button className="points-available-screen-borrow-button">
                  <button className="points-available-screen-button-content">
                    <span className="points-available-screen-text8">
                      傘を借りる
                    </span>
                  </button>
                  <img
                    src="/external/umbrella.svg"
                    alt="Umbrella5731"
                    className="points-available-screen-umbrella"
                  />
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <style jsx>
        {`
          .points-available-screen-container {
            width: 100%;
            display: flex;
            overflow: auto;
            min-height: 100vh;
            align-items: center;
            flex-direction: column;
          }
          .points-available-screen-points-available-screen {
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
          .points-available-screen-points-content {
            gap: 32px;
            width: 678px;
            height: 494px;
            display: flex;
            position: relative;
            align-items: center;
            flex-shrink: 0;
          }
          .points-available-screen-text1 {
            top: 37px;
            left: 195px;
            color: rgba(184, 28, 34, 1);
            height: auto;
            position: absolute;
            font-size: 48px;
            font-style: Bold;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 700;
            line-height: 33.599998474121094px;
            font-stretch: normal;
            text-decoration: none;
          }
          .points-available-screen-points-card {
            top: 124px;
            left: 39px;
            width: 600px;
            height: 400px;
            display: flex;
            padding: 40px;
            position: absolute;
            box-shadow: 0px 4px 20px 0px rgba(0, 0, 0, 0.062745101749897);
            align-items: flex-start;
            flex-shrink: 0;
            border-radius: 24px;
            justify-content: center;
            background-color: rgba(255, 255, 255, 1);
          }
          .points-available-screen-card-content {
            gap: 32px;
            top: 31px;
            left: 40px;
            width: 480px;
            height: 338px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
          }
          .points-available-screen-text2 {
            top: 9px;
            left: 24px;
            color: rgba(102, 102, 102, 1);
            height: auto;
            position: absolute;
            font-size: 32px;
            font-style: Medium;
            text-align: center;
            font-family: Noto Sans JP;
            white-space: nowrap;
            font-weight: 500;
            line-height: 21.600000381469727px;
            font-stretch: normal;
            text-decoration: none;
          }
          .points-available-screen-points-display {
            gap: 40px;
            top: 69px;
            left: 0px;
            width: 480px;
            height: 100px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            justify-content: space-between;
          }
          .points-available-screen-required-card {
            top: 0px;
            left: 0px;
            width: 120px;
            height: 100px;
            display: flex;
            padding: 16px;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 16px;
            flex-direction: column;
            justify-content: center;
            background-color: rgba(255, 245, 245, 1);
          }
          .points-available-screen-text3 {
            color: rgba(102, 102, 102, 1);
            height: auto;
            font-size: 14px;
            font-style: Medium;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 500;
            line-height: 16.799999237060547px;
            font-stretch: normal;
            text-decoration: none;
          }
          .points-available-screen-text4 {
            color: rgba(230, 0, 32, 1);
            height: auto;
            font-size: 28px;
            font-style: Bold;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 700;
            line-height: 33.599998474121094px;
            font-stretch: normal;
            text-decoration: none;
          }
          .points-available-screen-current-card {
            top: 0px;
            left: 360px;
            width: 120px;
            height: 100px;
            display: flex;
            padding: 16px;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 16px;
            justify-content: center;
            background-color: rgba(240, 253, 244, 1);
          }
          .points-available-screen-text5 {
            top: 24.5px;
            left: 18px;
            color: rgba(102, 102, 102, 1);
            height: auto;
            position: absolute;
            font-size: 14px;
            font-style: Medium;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 500;
            line-height: 16.799999237060547px;
            font-stretch: normal;
            text-decoration: none;
          }
          .points-available-screen-text6 {
            top: 41.5px;
            left: 34px;
            color: rgba(40, 167, 69, 1);
            height: auto;
            position: absolute;
            font-size: 28px;
            font-style: Bold;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 700;
            line-height: 33.599998474121094px;
            font-stretch: normal;
            text-decoration: none;
          }
          .points-available-screen-status-badge {
            top: 194px;
            left: 160px;
            width: 160px;
            height: 48px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 24px;
            justify-content: center;
            background-color: rgba(40, 167, 69, 1);
          }
          .points-available-screen-text7 {
            top: 14px;
            left: 48px;
            color: rgba(255, 255, 255, 1);
            height: auto;
            position: absolute;
            font-size: 16px;
            font-style: Black;
            text-align: left;
            font-family: Noto Sans JP;
            font-weight: 900;
            line-height: 19.200000762939453px;
            font-stretch: normal;
            text-decoration: none;
          }
          .points-available-screen-borrow-button {
            top: 266px;
            left: 40px;
            width: 400px;
            height: 72px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-shrink: 0;
            border-radius: 36px;
            justify-content: center;
            background-color: rgba(0, 91, 172, 1);
          }
          .points-available-screen-button-content {
            gap: 12px;
            top: 24px;
            left: 132px;
            width: 160px;
            display: flex;
            position: absolute;
            align-items: center;
          }
          .points-available-screen-text8 {
            color: rgba(255, 255, 255, 1);
            height: auto;
            font-size: 32px;
            font-style: Black;
            text-align: left;
            font-family: Noto Sans JP;
            white-space: nowrap;
            font-weight: 900;
            line-height: 24px;
            font-stretch: normal;
            text-decoration: none;
          }
          .points-available-screen-umbrella {
            top: 25px;
            left: 93px;
            width: 24px;
            height: 24px;
            position: absolute;
          }
        `}
      </style>
    </>
  )
}

export default PointsAvailableScreen
