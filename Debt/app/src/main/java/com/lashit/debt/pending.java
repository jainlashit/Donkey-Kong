package com.lashit.debt;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

/**
 * Created by lashit on 26/6/15.This is not an activity class ..this is just a base for our database
 */
public class pending {
    // This is identity key  of our sqlite
    public static final String KEY_ROWID = "_id";
    //Now we'll define some more id's for our database and we've used static final for strings coz we wanna set it as a constant string variable
    public static final String KEY_NAME = "name";
    public static final String KEY_AMOUNT = "amount";
    public static final String  KEY_DUE = "date";
    public static final String KEY_TYPE ="type";

    private static final String DATABASE_NAME ="DebtRecord";
    private static final String DATABASE_TABLE = "Record";
    private static final int DATABASE_VERSION = 1;

    private DB DBHelper;
    private final Context ContextHelper;
    private SQLiteDatabase DatabaseHelper;


    public pending(Context c)
    {
       ContextHelper = c;
    }

    public pending open()
    {
        DBHelper = new DB(ContextHelper);
        DatabaseHelper=DBHelper.getWritableDatabase();
        return this;
    }
    public void close()
    {
        DBHelper.close();
    }


    private static class DB extends SQLiteOpenHelper {
        public DB(Context context) {
            super(context,DATABASE_NAME, null, DATABASE_VERSION);
        }

        @Override
        public void onCreate(SQLiteDatabase db) {
            db.execSQL("CREATE TABLE "+ DATABASE_TABLE + " ("+
                    KEY_ROWID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + KEY_NAME + " TEXT NOT NULL, "+ KEY_AMOUNT + "TEXT NOT NULL, "
                    +KEY_TYPE + "TEXT NOT NULL, "+ KEY_DUE + "TEXT NOT NULL);"
            );
        }

        @Override
        public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
            db.execSQL("DROP TABLE IF EXISTS " + DATABASE_NAME);
            onCreate(db);
        }
    }
}
