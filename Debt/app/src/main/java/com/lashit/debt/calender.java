package com.lashit.debt;

import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.DatePicker;


public class calender extends ActionBarActivity {

    DatePicker due;
    Button next;
    Button prev;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calender);
        Intent intent = getIntent();
        String value = intent.getStringExtra("key");
        due =(DatePicker)findViewById(R.id.datePicker);
        due.setMinDate(System.currentTimeMillis()-1000);
        next=(Button)findViewById(R.id.button4);
        prev=(Button)findViewById(R.id.button3);
        next.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int day = due.getDayOfMonth();
                int month = due.getMonth() + 1;
                int year = due.getYear();
                String data = day + "/" + month + "/" + year;
                Intent pass = new Intent(calender.this,way.class);
                pass.putExtra("data", data);
                calender.this.startActivity(pass);
            }
        });
        prev.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent fail = new Intent(calender.this, MainActivity.class);
                fail.putExtra("null", 1);
                calender.this.startActivity(fail);
            }
        });
    }
}