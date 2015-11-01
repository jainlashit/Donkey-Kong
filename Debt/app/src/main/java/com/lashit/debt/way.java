package com.lashit.debt;

import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.RadioButton;


public class way extends ActionBarActivity {

    RadioButton give;
    RadioButton take;
    Button finish;
    Button back;
    int flag1=0;
    int flag2=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_way);
        give = (RadioButton)findViewById(R.id.button5);
        take = (RadioButton)findViewById(R.id.button6);
        take.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v)
            {
                if(flag1==0)
                    flag1=1;
                else
                    flag1=0;
                if(flag1==0)
                    take.setBackgroundResource(R.drawable.oval);
                else
                {
                    take.setBackgroundResource(R.drawable.oval_selected);
                    if (flag2 == 1)
                    {
                        flag2 = 0;
                        give.setBackgroundResource(R.drawable.oval);
                    }
                }
            }
        });
        give.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(flag2==0)
                    flag2=1;
                else
                    flag2=0;
                if (flag2 == 0)
                    give.setBackgroundResource(R.drawable.oval);
                else
                {
                    if(flag1==1)
                    {
                        flag1=0;
                        take.setBackgroundResource(R.drawable.oval);
                    }
                    give.setBackgroundResource(R.drawable.oval_selected);
                }
            }
        });
        back = (Button)findViewById(R.id.button3);
        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent back=new Intent(way.this,calender.class);
                back.putExtra("hello",0);
                way.this.startActivity(back);
            }
        });
        finish = (Button)findViewById(R.id.button4);
        finish.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent back = new Intent(way.this, core.class);
                back.putExtra("hello", 0);
                way.this.startActivity(back);
            }
        });
    }
}
