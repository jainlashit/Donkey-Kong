package com.lashit.debt;

import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;


public class MainActivity extends ActionBarActivity {

    Button next;
    EditText name;
    EditText amount;
    String naam;
    String daam;
    int flag=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        next= (Button)findViewById(R.id.button2);
        name=(EditText)findViewById(R.id.name);
        amount=(EditText)findViewById(R.id.amount);
        next.setOnClickListener(
                new View.OnClickListener() {
                    @Override
                    public void onClick(View v)
                    {

                        naam = name.getText().toString();
                        daam = amount.getText().toString();
                        if(naam.trim().equals("")||daam.trim().equals(""))
                        {
                            if (naam.trim().equals(""))
                                name.setError(" Field cannot be empty ");
                            else
                                name.setError(null);
                            if (daam.trim().equals(""))
                                amount.setError(" Field cannot be empty ");
                            else
                                amount.setError(null);
                        }
                        else
                        {
                            Intent calender = new Intent(MainActivity.this, calender.class);
                            calender.putExtra("key", 5);
                            MainActivity.this.startActivity(calender);
                            flag=1;
                        }
                    }
                }
        );
    }
}