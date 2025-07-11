import { NextResponse } from 'next/server';
import { spawn } from 'child_process';
import path from 'path';
import fs from 'fs';

const pythonPath = "C:\\Python313\\python.exe";

export async function POST() {
  try {
    console.log('APIルート: Pythonスクリプトを実行中...');
    
    // ファイルパスを絶対パスで指定
    const scriptPath = path.join(process.cwd(), 'app', 'api', 'run-python', 'test.py');
    console.log('Pythonスクリプトパス:', scriptPath);
    
    // ファイルが存在するかチェック
    if (!fs.existsSync(scriptPath)) {
      throw new Error(`Pythonスクリプトが見つかりません: ${scriptPath}`);
    }
    
    console.log('Pythonスクリプトファイルが存在することを確認しました');
    
    // Pythonの実行可能ファイルが存在するかチェック
    if (!fs.existsSync(pythonPath)) {
      throw new Error(`Python実行ファイルが見つかりません: ${pythonPath}`);
    }
    
    console.log('Python実行ファイルが存在することを確認しました');
    
    try {
      console.log(`実行コマンド: ${pythonPath} "${scriptPath}"`);
      
      const pythonProcess = spawn(pythonPath, [scriptPath]);
      
      let stdout = '';
      let stderr = '';
      
      // stdoutデータを収集
      pythonProcess.stdout.on('data', (data) => {
        stdout += data.toString();
        console.log('Python stdout chunk:', data.toString());
      });
      
      // stderrデータを収集
      pythonProcess.stderr.on('data', (data) => {
        stderr += data.toString();
        console.warn('Python stderr chunk:', data.toString());
      });
      
      // プロセスの終了を待つ
      const result = await new Promise((resolve, reject) => {
        pythonProcess.on('close', (code) => {
          console.log('Pythonプロセス終了コード:', code);
          if (code === 0) {
            resolve(stdout);
          } else {
            reject(new Error(`プロセスがコード${code}で終了: ${stderr}`));
          }
        });
        
        pythonProcess.on('error', (error) => {
          console.log('Pythonプロセスエラー:', error.message);
          reject(error);
        });
      });
      
      console.log('Python最終stdout:', result);
      
      // stdoutを行ごとに分割して、空でない行を取得
      const results = result.split('\n').filter(line => line.trim() !== '');
      console.log('処理済み結果:', results);
      
      if (results && results.length > 0) {
        return NextResponse.json({ 
          success: true, 
          studentID: results 
        });
      } else {
        return NextResponse.json({ 
          success: false, 
          error: '学生番号が取得できませんでした。' 
        }, { status: 400 });
      }
      
    } catch (error) {
      console.log('Pythonスクリプト実行でエラー:', error.message);
      throw error;
    }
    
  } catch (error) {
    console.error('Pythonスクリプト実行エラー:', error);
    return NextResponse.json({ 
      success: false, 
      error: error.message 
    }, { status: 500 });
  }
}
