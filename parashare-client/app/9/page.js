'use client'
import React from 'react'
import Head from 'next/head'


const Waitscreen = (props) => {
  return (
    <>
      <div className="waitscreen-container">
        <Head>
          <title>exported project</title>
        </Head>
        <div className="waitscreen-waitscreen">
          <div className="waitscreen-completion-card">
            <span className="waitscreen-text1">
              <span>システム処理中です</span>
              <br></br>
              <span>10秒程度お待ちください</span>
              <br></br>
            </span>
            <img
              src="/external/loader-circle.svg"
              alt="Ellipse16811"
              className="waitscreen-ellipse1"
            />
          </div>
        </div>
      </div>
      <style jsx>
        {`
          .waitscreen-container {
            width: 100%;
            display: flex;
            overflow: auto;
            min-height: 100vh;
            align-items: center;
            flex-direction: column;
          }
          .waitscreen-waitscreen {
            width: 100%;
            height: auto;
            display: flex;
            padding: 40px;
            align-items: center;
            flex-shrink: 0;
            flex-direction: column;
            justify-content: center;
            background-color: rgba(187, 187, 187, 0.7333333492279053);
          }
          .waitscreen-completion-card {
            width: 714px;
            height: 526px;
            display: flex;
            padding: 40px;
            position: relative;
            box-shadow: 0px 4px 20px 0px rgba(0, 0, 0, 0.062745101749897);
            align-items: center;
            flex-shrink: 0;
            border-radius: 24px;
            justify-content: center;
            background-color: rgba(255, 255, 255, 1);
          }
          .waitscreen-text1 {
            top: 180px;
            left: 50px;
            color: rgba(102, 102, 102, 1);
            width: 615px;
            height: auto;
            position: absolute;
            font-size: 48px;
            font-style: Bold;
            text-align: center;
            font-family: Noto Sans JP;
            font-weight: 700;
            line-height: 43.20000076293945px;
            font-stretch: normal;
            text-decoration: none;
          }
          .waitscreen-ellipse1 {
            top: 354px;
            left: 320px;
            width: 107px;
            height: 107px;
            position: absolute;
          }
        `}
      </style>
    </>
  )
}

export default Waitscreen
