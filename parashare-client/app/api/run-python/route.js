import { NextResponse } from 'next/server';
import { exec } from 'child_process';
import path from 'path';
import { promisify } from 'util';
import fs from 'fs';

const execAsync = promisify(exec);

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
    const pythonCommands = ['python', 'python3', 'py'];
    let result = null;
    let lastError = null;
    
    for (const pythonCmd of pythonCommands) {
      try {
        const command = `${pythonCmd} "${scriptPath}"`;
        console.log('試行中のコマンド:', command);
        
        const { stdout, stderr } = await execAsync(command);
        
        if (stderr) {
          console.warn(`${pythonCmd} stderr:`, stderr);
        }
        
        console.log(`${pythonCmd} stdout:`, stdout);
        result = stdout;
        break; // 成功したらループを抜ける
        
      } catch (error) {
        console.log(`${pythonCmd} でエラー:`, error.message);
        lastError = error;
        continue; // 次のコマンドを試す
      }
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
