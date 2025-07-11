import { NextResponse } from 'next/server';
import { spawn } from 'child_process';
import path from 'path';
import fs from 'fs';
const pythonCommands = "C:\\Users\\yama\\AppData\\Local\\Programs\\Python\\Python310\\python.exe";

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
    
    // 複数のPythonコマンドを試す
  
    let result = null;
    let lastError = null;
    
   
      try {
        
        pythonCmd = pythonCommands; // Pythonの実行コマンド
        const pythonProcess = spawn(pythonCmd, [scriptPath]);
        
        let stdout = '';
        let stderr = '';
        
        // stdoutデータを収集
        pythonProcess.stdout.on('data', (data) => {
          stdout += data.toString();
          console.log(`${pythonCmd} stdout chunk:`, data.toString());
        });
        
        // stderrデータを収集
        pythonProcess.stderr.on('data', (data) => {
          stderr += data.toString();
          console.warn(`${pythonCmd} stderr chunk:`, data.toString());
        });
        
        // プロセスの終了を待つ
        await new Promise((resolve, reject) => {
          pythonProcess.on('close', (code) => {
            console.log(`${pythonCmd} プロセス終了コード:`, code);
            if (code === 0) {
              resolve(stdout);
            } else {
              reject(new Error(`プロセスがコード${code}で終了: ${stderr}`));
            }
          });
          
          pythonProcess.on('error', (error) => {
            console.log(`${pythonCmd} プロセスエラー:`, error.message);
            reject(error);
          });
        });
        
        console.log(`${pythonCmd} 最終stdout:`, stdout);
        result = stdout;
        
        
      } catch (error) {
        console.log(`${pythonCmd} でエラー:`, error.message);
        lastError = error;
        
      }
    
    
    if (!result) {
      throw lastError || new Error('すべてのPythonコマンドが失敗しました');
    }
    
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
    console.error('Pythonスクリプト実行エラー:', error);
    return NextResponse.json({ 
      success: false, 
      error: error.message 
    }, { status: 500 });
  }
}
