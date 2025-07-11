"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function Page() {
    const [value, setValue] = useState(0);
    const router = useRouter();

    useEffect(() => {
        const timer = setTimeout(() => {
            setValue(1);
            router.push('/1'); // 1秒後に/1ページに移動
        }, 1000);
        return () => clearTimeout(timer);
    }, [router]);

    return (
        <div>
            <p>{value}</p>
        </div>
    );
}