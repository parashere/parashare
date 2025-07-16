-- ENUM定義（傘の状態）
CREATE TYPE PARASOL_STATUS AS ENUM (
  'available',
  'rented',
  'maintenance',
  'lost'
);

-- 傘テーブル
CREATE TABLE "parasol" (
  "id" UUID DEFAULT gen_random_uuid() NOT NULL,
  "rfid_id" VARCHAR(32) UNIQUE NOT NULL,
  "status" PARASOL_STATUS NOT NULL,
  "added_at" TIMESTAMPTZ NOT NULL,
  "created_at" TIMESTAMPTZ DEFAULT NOW(),
  "updated_at" TIMESTAMPTZ DEFAULT NOW(),
  PRIMARY KEY ("id")
);

-- 学生テーブル
CREATE TABLE "students" (
  "id" UUID DEFAULT gen_random_uuid() NOT NULL,
  "student_id" VARCHAR(16) UNIQUE NOT NULL,
  "created_at" TIMESTAMPTZ DEFAULT NOW(),
  "updated_at" TIMESTAMPTZ DEFAULT NOW(),
  PRIMARY KEY ("id")
);

-- 傘スタンドテーブル
CREATE TABLE "para_stand" (
  "id" UUID DEFAULT gen_random_uuid() NOT NULL,
  "version" VARCHAR(16) NOT NULL,
  "location" VARCHAR(64) NOT NULL,
  "created_at" TIMESTAMPTZ DEFAULT NOW(),
  "updated_at" TIMESTAMPTZ DEFAULT NOW(),
  PRIMARY KEY ("id")
);

-- レンタル履歴テーブル
CREATE TABLE "rental_history" (
  "id" UUID DEFAULT gen_random_uuid() NOT NULL,
  "students_id" UUID NOT NULL,
  "parasol_id" UUID NOT NULL,
  "rent_stand_from" UUID NOT NULL,
  "return_stand_to" UUID,
  "rented_at" TIMESTAMPTZ NOT NULL,
  "due_at" TIMESTAMPTZ NOT NULL,
  "returned_at" TIMESTAMPTZ,
  "created_at" TIMESTAMPTZ DEFAULT NOW(),
  "updated_at" TIMESTAMPTZ DEFAULT NOW(),
  PRIMARY KEY ("id"),
  CONSTRAINT "FK_rental_history.parasol_id"
    FOREIGN KEY ("parasol_id")
      REFERENCES "parasol"("id"),
  CONSTRAINT "FK_rental_history.students_id"
    FOREIGN KEY ("students_id")
      REFERENCES "students"("id"),
  CONSTRAINT "FK_rental_history.rent_stand_from"
    FOREIGN KEY ("rent_stand_from")
      REFERENCES "para_stand"("id"),
  CONSTRAINT "FK_rental_history.return_stand_to"
    FOREIGN KEY ("return_stand_to")
      REFERENCES "para_stand"("id")
);
