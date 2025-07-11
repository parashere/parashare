import { NextResponse } from 'next/server';
import { PythonShell } from 'python-shell';

export async function POST() {
  try {
    console.log('Pythonスクリプトを実行中...');
    
    const results = await new Promise((resolve, reject) => {
      PythonShell.run('./python/sample.py', null, (err, results) => {
        if (err) {
          reject(err);
        } else {
          resolve(results);
        }
      });
    });

    console.log(results);
    
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
