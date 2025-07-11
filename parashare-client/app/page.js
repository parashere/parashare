"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function Page() {
    const router = useRouter();

    useEffect(() => {
        const timer = setTimeout(() => {
            router.push('/1'); // 1秒後に/1ページに移動
        }, 1000);
        return () => clearTimeout(timer);
    }, [router]);

    return (
        <div>
            <p>立ち上げ中です 自動的に遷移します</p>
        </div>
    );
}